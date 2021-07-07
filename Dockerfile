FROM python:3-slim

WORKDIR /app

EXPOSE 8000

RUN pip install -U pip -U setuptools gunicorn uvicorn supervisor

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT mkdir -p pids logs \
        && python manage.py migrate \
        && python manage.py collectstatic --noinput \
        && supervisord -c supervisord.ini
