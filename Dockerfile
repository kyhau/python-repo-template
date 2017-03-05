MAINTAINER Kay Hau <virtualda@gmail.com>

# This implies using the following docker build black magic
# to make it work with different PIP indexes
# https://stackoverflow.com/questions/19537645/get-environment-variable-value-in-dockerfile
ENV PIP_INDEX_URL $PIP_INDEX_URL

ADD  .  /opt/apps/module
RUN ((cd /opt/apps/module && pip --no-cache-dir install -e .) && \
     rm -rf /root/.cache/pip)
