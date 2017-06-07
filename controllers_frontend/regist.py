# coding: utf-8

from base_controller import BaseController


class RegistController(BaseController):

    urls = r"/api/v1/register/?"

    def post(self):
        pass


class RegisterEmailController(BaseController):

    urls = r"/api/v1/register/email/verify/?([0-9A-Za-z]+)?/?([a-z]+)?/?"

    def get(self):
        pass
