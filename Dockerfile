FROM python:3.8-slim

LABEL maintainer="timerring"

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV TZ="Asia/Shanghai"

CMD ["python", "-m", "looplive.main"]