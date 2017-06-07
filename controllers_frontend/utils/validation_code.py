# -*- coding: UTF-8 -*-

import base64
import cStringIO
import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter

from base_controller import BaseController

from tools.db import get_redis_connection
from controllers_frontend.front_base_controller import LoginFreeBaseController


class ValidationCodeController(BaseController):

    urls = r"/api/v1/validation_code/?"

    def get(self):

        # source: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140767171357714f87a053a824ffd811d98a83b58ec13000
        # source: http://stackoverflow.com/questions/31826335/how-to-convert-pil-image-image-object-to-base64-string
        # source: https://github.com/lvziwen/generate-identify-code/blob/master/generate_identify_code.py

        # 随机字母:
        def rndChar():
            return chr(random.randint(65, 90))

        # 随机颜色1:
        def rndColor():
            return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

        # 随机颜色2:
        def rndColor2():
            return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

        # 240 x 60:
        width = 60 * 4
        height = 60
        image = Image.new('RGB', (width, height), (255, 255, 255))

        # 创建Font对象:
        font = ImageFont.truetype('./fonts/LiberationSerif-Bold.ttf', 36)

        # 创建Draw对象:
        draw = ImageDraw.Draw(image)

        # 填充每个像素:
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=rndColor())

        # 输出文字:
        char_list = [rndChar() for _ in range(4)]

        for t in range(4):
            draw.text((60 * t + 10, 10), char_list[t], font=font, fill=rndColor2())

        # 模糊:
        image = image.filter(ImageFilter.BLUR)

        buffer = cStringIO.StringIO()
        image.save(buffer, format="jpeg")
        img_str = base64.b64encode(buffer.getvalue())

        # 随机id
        validation_code_id = "".join([str(random.randint(1, 9)) for _ in range(10)])

        # 设置验证码过期时间60s
        redis = get_redis_connection()
        redis.setex(validation_code_id, "".join(char_list).upper(), 600)

        self.write(
            {
                "status": "SUCCESS",
                "code": 100,
                "data": {
                    "validation_code_id": int(validation_code_id),
                    "validation_code_img": img_str
                }
            }
        )

    def post(self):

        res_body = self.body_data

        if not res_body:
            raise_user_exc(StarErrorCode.REQUEST_PARAM_NONE)

        validation_code_id = res_body["validation_code_id"]
        validation_code_value = res_body["validation_code_value"].upper()

        redis = get_redis_connection()
        validation_code_value_cache = redis.get(validation_code_id)

        if not validation_code_value_cache:
            raise_user_exc(StarErrorCode.VALIDATION_CODE_OUT_OF_TIME)

        if validation_code_value_cache != validation_code_value:
            raise_user_exc(StarErrorCode.VALIDATION_CODE_ERROR)

        self.write({"status": "SUCCESS", "code": 100})
