FROM python:3.6.8

LABEL maintainer="pawissakan.cpcu@gmail.com"

RUN pip install cython

RUN pip install flask