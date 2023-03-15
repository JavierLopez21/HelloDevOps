FROM python:3.9-slim-buster AS build

RUN echo "deb http://security.debian.org/debian-security/buster/updates main" > /etc/apt/sources.list
RUN echo "deb http://deb.debian.org/debian/ buster-updates main" > /etc/apt/sources.list

WORKDIR /app

COPY . /app/

RUN pip3 install --upgrade pip
    
RUN pip --no-cache-dir install -r requirements.txt

RUN adduser --system --uid 10000 --group --shell /sbin/nologin --home /app/ app
RUN chmod -R 777 /app/src/app.py

EXPOSE 4000

USER 10000

CMD [ "python3" , "/app/src/app.py"]
