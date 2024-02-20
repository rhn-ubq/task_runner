from celery import Celery, Task
import time


# Configure Celery
app = Celery('task_runner', broker='pyamqp://guest@localhost//', backend='pyamqp://guest@localhost//')
app.config_from_object('celery_config')


# Define a class-based Celery task
@app.task(name='tasks.scheduled_task')
class ScheduledTask(Task):
    def run(self, *args, **kwargs):
        try:
            time.sleep(1)
            print("Task running!")
            # Simulate a time-consuming task
            time.sleep(5)
            print("Task finished")
        except Exception as exc:
            raise self.retry(exc=exc, countdown=60)


app.conf.beat_schedule = {'run-every-five-min': {'task': 'tasks.ScheduledTask.scheduled_task', 'schedule': 5.0*60}}
