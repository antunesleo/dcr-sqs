# dcr-sqs
Testing django-celery-results with sqs broker

## Install

```sh
$ pip install -r requirements.txt
$ python manage.py migrate
```

## Run

```sh
$ docker-compose up
$ celery --app dcrsqs.celery worker --loglevel=info
```

## Apply task

```sh
$ python manage.py shell
$ from dcrsqs.celery import add_numbers
$ add_numbers.delay(10, 5)
```

## Check Task Results

```sh
$ python manage.py shell
$ from django_celery_results.models import TaskResult
$ tr = TaskResult.objects.first()
$ tr.task_name, tr.task_args
```
