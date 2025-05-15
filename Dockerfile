FROM python:3.9

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
# install dependencies
RUN pip install --upgrade pip setuptools

RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 8000