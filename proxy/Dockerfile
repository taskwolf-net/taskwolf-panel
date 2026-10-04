ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/taskwolf-obfuscation:latest AS builder

RUN mkdir -p /home/taskwolf/panel
RUN ln -s /obfuscation /home/taskwolf/panel

COPY static /home/taskwolf/panel/static
COPY obfuscation /home/taskwolf/panel/obfuscation

ENV OBFUSCATION_HOME=/home/taskwolf/panel

RUN node /home/taskwolf/panel/obfuscation/obfuscate.js

FROM nginx

COPY --from=builder /home/taskwolf/panel/static /home/taskwolf/panel/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
COPY proxy/proxy /etc/nginx/sites-enabled/proxy
