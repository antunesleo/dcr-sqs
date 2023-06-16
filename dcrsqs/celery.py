from __future__ import absolute_import, unicode_literals

import os



# set the default Django settings module for the 'celery' program.
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcrsqs.settings")

app = Celery("dcrsqs")

app.config_from_object(settings.CELERY)
app.autodiscover_tasks()


@app.task
def add_numbers(a, b):
    result = a + b
    print(f'result: {result}')
    return result
