FROM ubuntu:16.04

# Python with pip
RUN apt-get update && apt-get install -y python-dev python python-pip
RUN pip install pip --upgrade

# Python deps
RUN pip --no-cache-dir install pyzmq
RUN pip --no-cache-dir install absl-py

# This
ENV WORK_DIR /root/work

RUN mkdir -p ${WORK_DIR}

WORKDIR ${WORK_DIR}
COPY learner_v2.py .
COPY actor_v2.py .

