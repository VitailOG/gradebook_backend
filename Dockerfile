FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN apk update \
    && apk add postgresql-dev musl-dev postgresql-client

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

COPY . .
