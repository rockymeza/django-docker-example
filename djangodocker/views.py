from django.http import HttpResponse

from djangodocker.celery import debug_task


def add_celery_task(request, *args, **kwargs):
    debug_task.delay()
    return HttpResponse('Hi')
