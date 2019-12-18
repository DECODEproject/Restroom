FROM dyne/devuan:beowulf
ENV debian buster

LABEL maintainer="Puria Nafisi Azizi <puria@dyne.org>" \
      homepage="https://github.com/DECODEroject/Restroom"

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV RESTROOM_CONFIG_FILE /sample/config

RUN apt-get update -y -q \
    && apt-get install -y -q \
    pkg-config \
    python3 \
    python3-pip \
    python3-dev \
    && apt-get clean

RUN pip3 install --upgrade pip
RUN pip install hypercorn
RUN pip install setuptools
COPY src /app
COPY sample /sample
RUN pip install -e /app

WORKDIR /app
CMD hypercorn -b 0.0.0.0:8000 app:app
