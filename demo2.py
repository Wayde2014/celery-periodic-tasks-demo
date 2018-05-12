# coding=utf-8

"""
    demo2 can work well with celery==3.1.25 and celery==4.1.0
"""

import logging
from datetime import timedelta

from celery import Celery
from celery.signals import setup_logging

from log_util import LogUtil


app = Celery('task_demo2', broker='redis://127.0.0.1:6379/1')

app.conf.beat_schedule = {
    'minus-every-5-second': {
        'task': 'demo2.minus',
        'schedule': timedelta(seconds=5),
        'args': (3, 2)
    },
}
app.conf.timezone = 'Asia/Shanghai'

# add logging config
conf = {
    'filename': 'log/demo2.log',
    'level': 'DEBUG',
}
LogUtil(**conf)

fn = lambda **kwargs: logging.getLogger()
setup_logging.connect(fn)


@app.task
def minus(x, y):
    logging.debug('calculate {0} minus {1} equals {2}'.format(x, y, x - y))
    return x - y
