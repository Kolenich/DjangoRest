FROM python:3.7.3-slim

LABEL maintainer="nick.zhigalin@gmail.com"

ENV PROJECT_MODE production

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT python manage.py migrate\
        && gunicorn backend.wsgi -b 0.0.0.0:8000