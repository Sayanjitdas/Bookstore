# pull base image
FROM python:3.8

# envs 
ENV PYTHONDONTWRTIEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#workdir

WORKDIR /app/

#install dependecies
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system

#COPY PROJECT
COPY . /app/
