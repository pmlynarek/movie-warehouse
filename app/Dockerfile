FROM python:3.8.2-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN pip install --upgrade pip
COPY requirements/ /app/requirements
RUN pip install -r requirements/staging.txt

COPY google_storage_key.json /app/google_storage_key.json

COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN useradd gunicorn
USER gunicorn

CMD gunicorn moviewarehouse.wsgi:application --bind 0.0.0.0:$PORT
