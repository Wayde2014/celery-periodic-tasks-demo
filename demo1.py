# coding=utf-8

"""
    demo1 can only work well with celery==3.1.25
"""

import logging
from datetime import timedelta

from celery import Celery
from celery.signals import setup_logging

from log_util import LogUtil


app = Celery('task_demo1', broker='redis://127.0.0.1:6379/0')

# add logging config
conf = {
    'filename': 'log/demo1.log',
    'level': 'DEBUG',
}
LogUtil(**conf)

fn = lambda **kwargs: logging.getLogger()
setup_logging.connect(fn)


CELERYBEAT_SCHEDULE = {
    'add-every-10-second': {
        'task': 'demo1.add',
        'schedule': timedelta(seconds=10),
        'args': (3, 2)
    },
}
CELERY_TIMEZONE = 'Asia/Shanghai'


@app.task
def add(x, y):
    logging.debug('calculate {0} plus {1} equals {2}'.format(x, y, x + y))
    return x + y
