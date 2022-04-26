# Flask Docker

## Docker File (Make A Docker Image)
___
### Dockerfile
```
FROM python:3-alpine
RUN pip install --upgrade pip
RUN mkdir app
COPY . /app
WORKDIR /app
ENV FLASK_APP=run.py
RUN python3 -m venv tutorial-env
RUN . tutorial-env/bin/activate
RUN pip install -r requirements.txt
CMD flask run --host 0.0.0.0
```
## Docker Compose (Run Docker Container)

### docker-compose.yaml
___

```
version: '3'
services:
  flaskrun:
    image: test_flask_4
```

## Commend For Make a docker Image
```
sudo docker build -t Dockerfile
```
### Commend For Run Cocker Container
```
sudo docker-compose -f docker-compose.yaml up

```