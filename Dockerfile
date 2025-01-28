FROM python:3

RUN apt-get update && apt-get install -y gettext && apt-get clean

RUN pip install django
RUN pip install gunicorn
RUN pip install django-cors-headers
RUN pip install requests
RUN pip install jwt

COPY . .

RUN django-admin compilemessages

ENTRYPOINT ["gunicorn","--config","app/gunicorn-config.py", "app.wsgi"]