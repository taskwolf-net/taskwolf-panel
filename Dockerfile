FROM registry.dulno.com/dulno-obfuscation:latest AS builder

RUN ln -s /obfuscation /panel

COPY . /panel

WORKDIR /panel

ENV OBFUSCATION_HOME=/panel

RUN node obfuscation/obfuscate.js

FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends gettext linux-libc-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir django gunicorn django-cors-headers requests jwt

COPY --from=builder /panel /panel

WORKDIR /panel

RUN django-admin compilemessages

ENTRYPOINT ["gunicorn", "--config","app/gunicorn-config.py", "app.wsgi"]