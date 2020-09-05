<p align="center">
  <img width="350" height="200" src="https://github.com/jgphilpott/agility/blob/master/app/imgs/icon.png">
</p>

# Agility

A Python library for humanoid robotics.

# Quick Start

Assuming you have [docker installed](https://docs.docker.com/get-docker), clone this repository and navigate into the root directory.

To build the agility container enter the command:

```
sudo docker build -t agility:latest .
```

To run the agility container enter the command:

```
sudo docker run -p 4444:4444 agility:latest
```
