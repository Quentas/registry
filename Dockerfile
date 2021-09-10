# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /register

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apk add --update \
  build-base \
  cargo \
  gcc \
  libffi-dev \
  musl-dev \
  openssl-dev \
  postgresql-client \
  postgresql-dev \
  py-cffi \
  rust 

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps


# to fix the cryptography package problem
#RUN apk add --update alpine-sdk && apk add libffi-dev openssl-dev
#RUN pip install cryptography

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser
