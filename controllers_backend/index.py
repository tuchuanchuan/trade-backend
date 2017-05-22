# coding: UTF-8

import settings
from controllers_backend.backend_base_controller import BaseController


class IndexController(BaseController):
    urls = '/index/?'

    description = {'GET': '首页'}

    def get(self):
        self.render('index.html')
