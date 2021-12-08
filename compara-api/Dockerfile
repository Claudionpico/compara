FROM alpine:3.10.3

LABEL mantainer="claudionpico@gmail.com"

ENV TERM xterm

RUN apk update
RUN apk add python py2-pip uwsgi uwsgi-python py-mysqldb
RUN mkdir -p /opt/compara-api

RUN apk add --no-cache tzdata
ENV TZ America/Argentina/Buenos_Aires

WORKDIR /opt/compara-api
COPY src/ /opt/compara-api/

RUN pip install "pip==19.3.1"
RUN pip install -U setuptools
RUN pip install -r requirements.txt

USER 1000:1000

CMD uwsgi --ini /opt/compara-api/compara-api.ini

EXPOSE 8000
