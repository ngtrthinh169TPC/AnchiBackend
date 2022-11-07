FROM python:3.8-alpine

WORKDIR /app

RUN apk add --no-cache build-base libffi-dev libxslt-dev libpq-dev

COPY requirements.txt requirements.txt


RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]