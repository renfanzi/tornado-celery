#!/usr/bin/env python
# -*-  coding:utf-8 -*-

import tornado.gen
from tornado.web import RequestHandler


class BaseRequest(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseRequest, self).__init__(application, request, **kwargs)

    @tornado.gen.coroutine
    def celery_task(self, func, params, queue="default_analysis"):
        response = yield tornado.gen.Task(func, args=params, queue=queue)
        raise tornado.gen.Return(response)
