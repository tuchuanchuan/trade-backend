# -*- coding: UTF-8 -*-

import base64
import cStringIO
import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter


class VerificationCode(object):
    def rndChar():
        return chr(random.randint(65, 90))

    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    def rndColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
