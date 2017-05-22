# coding: UTF-8

import settings
from controllers_backend.backend_base_controller import BaseController


class HealthCheckController(BaseController):
    urls = '/health_check/?'

    def prepare(self):
        pass

    def get(self):
        self.write(dict(ret=0))
