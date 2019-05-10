FROM python:3.7.3-slim

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT python manage.py migrate\
        && gunicorn backend.wsgi -b 0.0.0.0:8000