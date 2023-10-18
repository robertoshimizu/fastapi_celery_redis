import time
from celery import Celery

# Setting up Celery with Redis as the broker and result backend
celery_app = Celery("tasks",
                   broker="redis://localhost:6379/0",
                   backend="redis://localhost:6379/1")
@celery_app.task
def compute_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list

@celery_app.task
def long_fake_api(n=30):
    time.sleep(n)
    return n