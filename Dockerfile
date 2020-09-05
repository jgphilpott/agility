FROM docker.pkg.github.com/jgphilpott/docker-images/pi-pack:v1

RUN pip install RPi.GPIO

ADD . /root

WORKDIR /root

CMD ["python3", "app/root.py"]
