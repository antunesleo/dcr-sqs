# dcr-sqs
Testing django-celery-results with sqs broker

## Install

```sh
$ pip install -r requirements.txt
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