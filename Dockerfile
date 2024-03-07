FROM python:3.12.1-slim-bullseye
LABEL authors="EonBotz 5"
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY ../requirements.txt /app/
RUN pip install -r requirements.txt

COPY .. /app

ENTRYPOINT [ "gunicorn", "core.wsgi"]
