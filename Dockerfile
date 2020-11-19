# pull official base image
FROM python:3.7.9

# set work dir
WORKDIR /mymdb

# Set env variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements* /mymdb/
RUN pip install -r requirements.dev.txt

COPY . /mymdb/