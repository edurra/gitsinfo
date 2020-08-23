import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gitsinfo.settings")
app = Celery("gitsinfo", broker="amqp://rabbit//")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "gitsinfoapp.tasks.add",
        "schedule": 30.0
    }
}
