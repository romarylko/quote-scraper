FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY Pipfile* /app/

RUN pip install pipenv \
    && pipenv install --deploy --system --ignore-pipfile

COPY . /app/