FROM ubuntu:22.10
LABEL maintainer="virtualda@gmail.com"
ARG PIP_INDEX_URL

ADD  .  /opt/apps/module

# Install module
RUN ((cd /opt/apps/module && python3 -m pip --no-cache-dir install -e .) && \
     rm -rf /root/.cache/pip)

# Call module's main entry point/script defined in setup.py
#CMD ["run_module"]
