FROM docker.pkg.github.com/jgphilpott/docker-images/pi-pack-mini:v1

ADD . /root

WORKDIR /root

CMD ["python3", "root.py"]
