FROM jgphilpott/pi-pack:mini

ADD . /root

WORKDIR /root

CMD ["python3", "app/root.py"]
