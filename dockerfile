# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /cloudsek_project
RUN pip3 install virtualenv
RUN virtualenv env
ENV VIRTUAL_ENV /env                     
ENV PATH /env/bin:$PATH 
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . /cloudsek_project/
CMD python3 manage.py runserver 0.0.0.0:8000