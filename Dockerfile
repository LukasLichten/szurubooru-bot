FROM python:3-alpine as prereqs

RUN mkdir -p /opt/app
COPY ./ /opt/app/
WORKDIR /opt/app/

# Prerequists for python pillow to compile
RUN apk add --no-cache build-base zlib zlib-dev jpeg-dev
ENV LIBARY_PATH=/lib:/usr/lib

RUN pip3 install --no-python-version-warning --no-cache-dir -r requirements.txt
RUN rm requirements.txt

# Set up Tesseract-OCR
RUN apk add --no-cache tesseract-ocr
RUN apk add --no-cache tesseract-ocr-data-deu tesseract-ocr-data-chi_sim tesseract-ocr-data-jpn

RUN mkdir tmp/

ENTRYPOINT [ "python3", "-m", "docker_entry" ]