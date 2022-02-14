FROM python:3-slim as prereqs

RUN mkdir -p /opt/app
COPY ./ /opt/app/
WORKDIR /opt/app/

RUN pip3 install --no-python-version-warning --no-cache-dir -r requirements.txt
RUN rm requirements.txt

ENTRYPOINT [ "python3", "-m", "docker_entry" ]