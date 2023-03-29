FROM python:3.9-slim-buster AS build

ENV CONTAINER_HOME=/app

RUN echo "deb http://security.debian.org/debian-security/buster/updates main" > /etc/apt/sources.list
RUN echo "deb http://deb.debian.org/debian/ buster-updates main" > /etc/apt/sources.list

WORKDIR /app
COPY . /app/

RUN pip3 install --upgrade pip
    
RUN pip --no-cache-dir install -r requirements.txt
