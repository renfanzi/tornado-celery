#!/usr/bin/env python
# -*-  coding:utf-8 -*-
import tcelery
from tornado.ioloop import IOLoop
from tornado.web import Application
from handlers.data_handlers import *

Handlers = [
    (r"/a/(.*)", MineHandler),
    (r"/ye", MainHandler),
]

if __name__ == "__main__":
    tcelery.setup_nonblocking_producer()
    application = Application(Handlers)
    application.listen(port=8888, address="0.0.0.0")
    IOLoop.instance().start()
