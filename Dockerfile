FROM ubuntu:16.04
LABEL maintainer="virtualda@gmail.com"
ARG PIP_INDEX_URL

ADD  .  /opt/apps/module

# Install module
RUN ((cd /opt/apps/module && pip --no-cache-dir install -e .) && \
     rm -rf /root/.cache/pip)

