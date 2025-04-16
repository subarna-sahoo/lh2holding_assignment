from celery import Celery
import os

def make_celery():
    celery = Celery(
        'rss_summarizer',
        broker=os.getenv("CELERY_BROKER_URL"),
        backend=os.getenv("CELERY_RESULT_BACKEND"),
        include=["utils.tasks"]
    )

    # Register beat schedule
    celery.conf.beat_schedule = {
        'fetch-feeds-every-5-minutes': {
            'task': 'utils.tasks.fetch_and_queue_articles',
            'schedule': 300.0,  # every 5 minutes
        },
    }

    celery.conf.timezone = 'Asia/Kolkata'
    return celery

celery = make_celery()
