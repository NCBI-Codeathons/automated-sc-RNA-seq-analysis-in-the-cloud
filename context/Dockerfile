# this is a Dockerfile
# build Dockerimage
# run Dockerimage with the files we have pulled down
# check output is what we want the output to be


FROM python:3.9.0a2-alpine3.10

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
