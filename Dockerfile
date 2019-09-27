FROM python:3.7-slim-stretch

LABEL maintainer='nick.zhigalin@gmail.com'

WORKDIR /app

EXPOSE 8000

RUN pip install --upgrade pip \
 && pip install gunicorn

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT mkdir -p pids logs \
        && python manage.py migrate \
        && python manage.py collectstatic --noinput \
        && celery multi start worker -A backend --pidfile="pids/celery.pid" --logfile="logs/celery.log" \
        && gunicorn backend.wsgi -b 0.0.0.0:8000 -p pids/gunicorn.pid --access-logfile logs/gunicorn-access.log --log-file logs/gunicorn.log
