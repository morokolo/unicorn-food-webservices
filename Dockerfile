FROM python:3.5.2
MAINTAINER Team Green

# prevent dpkg error

ENV TERM=xterm-256color
ENV PYTHONUNBUFFERED 1
ENV WITH_DOCKER True

RUN apt-get update && apt-get install -qy --no-install-recommends binutils libproj-dev gdal-bin python-dev python3-lxml \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install virtualenv
RUN pip install -U pip setuptools wheel

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

