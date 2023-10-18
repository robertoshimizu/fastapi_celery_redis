# FASTAPI - CELERY - REDIS

## Description
This is a simple example of how to use celery with fastapi and redis as broker.

## Installation Celery
```bash
pip install celery
```

## Installation Redis
```bash
pip install redis
```
## First Steps
1. Create a file called `celery.py` and add the following code:
```python
from celery import Celery

app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=['celery_tasks.tasks']
)

app.conf.update(
    result_expires=3600,
)
```

in a terminal, start redis:
```bash
redis-server
```
Also in another terminal, start celery:
```bash
celery -A app.celery.celery_app worker --loglevel=info
```


