FROM tiangolo/uwsgi-nginx:python3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app
RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt

COPY . /app


