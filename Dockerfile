FROM python:3.8.6-buster

COPY twitterelectionbr /twitterelectionbr
COPY requirements_docker.txt /requirements.txt

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn twitterelectionbr.interface.api.twiitter:app --host 0.0.0.0
