// This file sets up the containerized environment for our code via Docker

FROM continuumio/anaconda3:latest

WORKDIR /app

ADD . /app

RUN conda update -n base -c defaults conda

RUN conda env create -f environment.yml 

RUN conda clean -a -y

