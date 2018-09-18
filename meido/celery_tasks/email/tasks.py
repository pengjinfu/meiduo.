from celery_tasks.main import app


@app.task()
def send_email():
    print(1111)
