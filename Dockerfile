FROM python:3.7-slim-buster

WORKDIR /flask_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .
COPY flask_app/ ./

CMD [ "python", "app.py" ]