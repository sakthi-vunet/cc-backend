# syntax=docker/dockerfile:1
FROM python:3.8.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY env/lib/python3.8/site-packages/docker /code/
# ENV PYTHONPATH "${PYTHONPATH}:/code/"
RUN pip install -r requirements.txt 
RUN pip install docker
COPY . /code/
# FROM mysql:5.6

# COPY /home/sakthi/testappsql /docker-entrypoint-initdb.d
