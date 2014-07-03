import os

BROKER_URL = 'amqp://{user}:{password}@{host}:{port}'.format(
    user='admin',
    password=os.environ['RABBITMQ_PASS'],
    host=os.environ['RABBITMQ_1_PORT_5672_TCP_ADDR'],
    port=os.environ['RABBITMQ_1_PORT_5672_TCP_PORT'],
)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
