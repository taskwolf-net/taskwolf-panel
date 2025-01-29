FROM registry.dulno.com/dulno-obfuscation:latest AS builder

RUN mkdir -p /home/dulno/panel
RUN ln -s /obfuscation /home/dulno/panel

COPY static /home/dulno/panel/static
COPY obfuscation /home/dulno/panel/obfuscation

ENV OBFUSCATION_HOME=/home/dulno/panel

RUN node /home/dulno/panel/obfuscation/obfuscate.js

FROM alpine
COPY --from=builder /home/dulno/panel/static /static/