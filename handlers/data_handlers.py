#!/usr/bin/env python
# -*-  coding:utf-8 -*-

import json
import tornado
from core.base import BaseRequest
from tasks.data_analysis import *


class MineHandler(BaseRequest):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        args = ["12345"]
        response = self.celery_task(single_celery.apply_async, params=args)
        print response
        print response.result
        self.write("hello world111")


def a(x, y):
    return x + y

def echo(message, callback):
    res = a(*message)
    callback(message, res)

class MainHandler(tornado.web.RequestHandler):
    # @tornado.gen.coroutine
    def get(self):
        response = yield tornado.gen.Task(echo, [1, 2])
        print response
        self.write(json.dumps(response.args[1]))



