FROM continuumio/anaconda3:latest

WORKDIR /app

ADD . /app

RUN conda update -n base -c defaults conda

RUN conda env create -f environment.yml 

RUN conda clean -a -y

CMD xvfb run -s "-screen 0 1400x900x24" conda run -n Gliese_22 python hello.py

