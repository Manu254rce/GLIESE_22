FROM continuumio/anaconda3:latest

WORKDIR /app

ADD . /app

RUN conda update -n base -c defaults conda

RUN conda env create -f environment.yml 

RUN conda clean -a -y

