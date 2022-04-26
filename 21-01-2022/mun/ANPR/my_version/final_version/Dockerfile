FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.7 python3-distutils python3-pip python3-apt
RUN apt-get update
RUN apt install -y libgl1-mesa-glx

RUN pip3 install -U pip
RUN pip3 install virtualenv

ENV FLASK_APP=bangla_car_plate_detection_and_recognition_api.py

RUN mkdir app
COPY . /app
WORKDIR /app

RUN virtualenv tutorial-env
RUN pip3 install -U pip
RUN . tutorial-env/bin/activate

RUN pip3 install -r requirements2.txt

CMD python3 bangla_car_plate_detection_and_recognition_api.py