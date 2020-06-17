FROM python:3.8-slim

WORKDIR /app

EXPOSE 8000

RUN pip install --upgrade pip setuptools \
 && pip install gunicorn

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT mkdir -p pids logs \
        && python manage.py migrate \
        && python manage.py collectstatic --noinput \
        && celery multi start worker -A backend --pidfile="pids/celery.pid" --logfile="logs/celery.log" \
        && gunicorn backend.wsgi -b 0.0.0.0 --access-logfile - --log-file -
