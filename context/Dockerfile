# this is a Dockerfile
# build Dockerimage
# run Dockerimage with the files we have pulled down
# check output is what we want the output to be


FROM continuumio/miniconda3
RUN apt-get update
RUN apt-get -y install libc-dev
RUN apt-get -y install libc6-dev
RUN conda update -n base -c defaults conda
RUN conda install -c anaconda gcc

#RUN apt updated
#RUN apt install build-essential

# COPY requirements-freeze.txt .
# RUN pip install  -r ./requirements-freeze.txt

# In development, you may want to pin a single dependency in requirements.txt,
# without throwing away the entire cache layer from requirements-freeze.txt.
# (But once it works, you should check in an updated freeze!)

COPY requirements.txt .
RUN pip install  -r ./requirements.txt
COPY . .
CMD [ "python", "processing.py", \
      "--input", "/input", \
      "--output", "/output" ]
