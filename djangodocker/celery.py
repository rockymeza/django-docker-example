from __future__ import absolute_import, print_function

import os

from celery import Celery

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangodocker.settings")

app = Celery('djangodocker')

app.config_from_object('djangodocker.settings_celery')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
