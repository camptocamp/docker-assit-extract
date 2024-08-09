FROM ubuntu:oracular AS builder

LABEL Maintainer="andrey.rusakov@camptocamp.com" Vendor="Camptocamp"

WORKDIR /geoshop

RUN apt update && \
    apt upgrade -y && \
    apt install -y bash postgresql curl python3 python3-pip git libgdal-dev libffi-dev && \
    git clone https://github.com/camptocamp/geoshop-back.git /geoshop/geoshop-back && \
    cd /geoshop/geoshop-back && \
    pip3 install -r requirements.txt --break-system-packages

# FIXME: Add this through the containder od the composition
COPY .env /geoshop/geoshop-back/.env
COPY settings.py /geoshop/geoshop-back/settings.py
COPY resource/sampledata.sql /geoshop/sampledata.sql
COPY entrypoint.sh /geoshop/entrypoint.sh

ENTRYPOINT [ "/geoshop/entrypoint.sh" ]
