FROM python:3.8-slim

WORKDIR /app

EXPOSE 8000

RUN pip install -U pip -U setuptools \
 && pip install gunicorn

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT mkdir -p pids logs \
        && python manage.py migrate \
        && python manage.py collectstatic --noinput \
        && gunicorn backend.wsgi -b 0.0.0.0 --access-logfile - --log-file - -D \
        && python manage.py process_tasks
