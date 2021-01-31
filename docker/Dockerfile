FROM python:3.9.1-alpine3.12

CMD apk --update --no-cache add \
uwsgi

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "tail", "-f", "/dev/null" ]