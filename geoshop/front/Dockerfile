# Build with node
FROM node:22.6.0-slim AS builder
WORKDIR /usr/src/app

RUN apt update && \
    apt upgrade -y && \
    apt install -y git && \
    git clone https://github.com/camptocamp/geoshop-front.git . && \
    npm ci

COPY config.json src/assets/configs/config.json

RUN npm run build

# Serve with nginx unpprevileged
FROM nginxinc/nginx-unprivileged:stable

# copy server config
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Copy build artifacts
COPY --from=builder /usr/src/app/dist/ /usr/share/nginx/html
