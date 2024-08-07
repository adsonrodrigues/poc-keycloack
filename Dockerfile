FROM tiangolo/meinheld-gunicorn:python3.8

ENV MODULE_NAME core
ENV APP_MODULE=core.wsgi

COPY . /app/
WORKDIR /app

ADD Procfile /Procfile

COPY deploy/gunicorn_config.py /app/gunicorn_conf.py

COPY deploy/before.sh /app/prestart.sh
COPY deploy/start.sh /app/start.sh

RUN pip install -r requirements.txt

EXPOSE 80

RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]