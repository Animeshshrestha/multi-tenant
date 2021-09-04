FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt update -y
RUN apt install -y python3-pip python-dev build-essential


WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/
