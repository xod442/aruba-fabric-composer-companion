FROM ubuntu:latest
MAINTAINER Rick Kauffman "chewie@wookieware.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN mkdir /antigua

WORKDIR /antigua

ADD . .

RUN pip install -r requirements.txt

EXPOSE 5001

CMD python manage.py runserver
