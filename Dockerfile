FROM python:3.9-slim-buster

WORKDIR /app
RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]