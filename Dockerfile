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
# RUN apk add --no-cache tesseract-ocr-data-deu tesseract-ocr-data-chi_sim tesseract-ocr-data-jpn

# Adding best trained files
RUN apk add --no-cache wget
RUN wget -q https://github.com/tesseract-ocr/tessdata_best/raw/main/eng.traineddata
RUN mkdir -p /usr/share/tessdata
RUN mv eng.traineddata /usr/share/tessdata/eng_best.traineddata

# Adding a tmp folder for image processing
RUN mkdir tmp/

ENTRYPOINT [ "python3", "-m", "docker_entry" ]