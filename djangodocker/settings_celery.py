import os

BROKER_URL = 'amqp://admin:docker@{host}:{port}'.format(
    host=os.environ['RABBITMQ_1_PORT_5672_TCP_ADDR'],
    port=os.environ['RABBITMQ_1_PORT_5672_TCP_PORT'],
)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
