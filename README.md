# Security controller

## Description
This is a security controller for the SDN network. It is based on the [Ryu](https://osrg.github.io/ryu/) SDN controller framework.
The controller is able to detect and mitigate attacks on the network. It is also able to detect and mitigate attacks on the controller itself.
Its written in Python 3.11 and uses Django 3.2.8 as a web framework.

## Installation

### Requirements
- Python 3.11
- Django 3.2.8

### Docker
The easiest way to run the controller is to use the provided Dockerfile. To build the image run:
```bash
docker build -t security-controller .
```
To run the container:
```bash
docker run -p 8080:8080 security-controller
```
The controller will be available at http://localhost:8080

### Manual
To run the controller manually, first install the requirements:
```bash
pip install -r requirements.txt
```
Migrate the database:
```bash
python manage.py migrate
```

Then run the controller:
```bash
python manage.py runserver
```
The controller will be available at http://localhost:8080

## Usage
The controller has a web interface that can be used to configure it. It is available at http://localhost:8080/admin
