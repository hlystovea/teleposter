FROM python:3.12-slim
WORKDIR /teleposter
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./src ./src