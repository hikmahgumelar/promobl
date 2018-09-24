FROM ubuntu:16.04

MAINTAINER hikmahgumelar@gmail.com

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app


COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "src/app.py" ]