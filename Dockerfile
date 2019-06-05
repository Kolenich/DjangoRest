FROM python:3.7.3-slim

LABEL maintainer="nick.zhigalin@gmail.com"

ENV PROJECT_MODE production

WORKDIR /app

EXPOSE 8000

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT python manage.py migrate \
        && python manage.py collectstatic \
        && gunicorn backend.wsgi -b 0.0.0.0:8000
