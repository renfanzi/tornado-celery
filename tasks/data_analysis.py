#!/usr/bin/env python
# -*-  coding:utf-8 -*-
from celery import Celery


celery = Celery(
    'tasks.data_analysis',
    broker='amqp://192.168.72.131:5672',
    backend='amqp://192.168.72.131:5672',
    include='tasks.data_analysis'
)
celery.conf.CELERY_RESULT_BACKEND = "amqp://192.168.72.131:5672"
celery.conf.CELERY_ACCEPT_CONTENT = ['application/json']
celery.conf.CELERY_TASK_SERIALIZER = 'json'
celery.conf.CELERY_RESULT_SERIALIZER = 'json'
celery.conf.BROKER_HEARTBEAT = 30
celery.conf.CELERY_IGNORE_RESULT = False  # this is less important

class SFV():
    def do_(self, *args):
        return "c", "b", "a"


@celery.task()
def single_celery(*args):
    return SFV().do_(*args)

