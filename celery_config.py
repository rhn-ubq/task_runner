# celery_config.py
from kombu import Exchange, Queue

broker_url = 'pyamqp://guest@localhost//'
result_backend = 'pyamqp://guest@localhost//'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

timezone = 'UTC'

enable_utc = True

task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
)
