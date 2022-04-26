from datetime import datetime
from django.conf import settings
import numpy as np
from decouple import config
import paho.mqtt.client as mqtt
import cv2
import json
import base64
import django
django.setup()
if settings.MQTT == True:
    from forbidden_activity.models import *


class MQTTClient:
    def __init__(self):
        self.broker = '192.168.1.231'
        self.port = 1883
        self.worker_count_ml_topic = "worker_count_ml_topic"
        self.forbidden_activity_ml_topic = "forbidden_activity_ml_topic"
        self.fixed_place_people_count_ml_topic = "fixed_place_people_count_ml_topic"
        self.client_id = "worker_count_backend_id"

    def run(self):
        # The callback for when the client receives a CONNACK response from the server.
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code "+str(rc))

            # Subscribing in on_connect() means that if we lose the connection and
            # reconnect then subscriptions will be renewed.
            # client.subscribe(self.topic)
            client.subscribe([
                (self.worker_count_ml_topic, 0),
                (self.forbidden_activity_ml_topic, 1),
                (self.fixed_place_people_count_ml_topic, 2)
            ])

        # The callback for when a PUBLISH message is received from the server.
        def on_message(client, userdata, msg):
            if msg.topic == self.worker_count_ml_topic:
                # byte_to_json = json.loads(msg.payload.decode('utf-8'))
                print(msg.payload)
                # print(byte_to_json)
                # if byte_to_json["enter"] > 0:
                #     Entry.objects.create(
                #         time=byte_to_json["time"], person=byte_to_json["enter"])
                # if byte_to_json["exit"] > 0:
                #     Exit.objects.create(
                #         time=byte_to_json["time"], person=byte_to_json["exit"])
            if msg.topic == self.forbidden_activity_ml_topic:
                byte_to_json = json.loads(msg.payload.decode('utf-8'))
                print("byte_to_json----",byte_to_json)
                ForbiddenActivity.objects.create(
                    worker_uuid=byte_to_json["name"] if byte_to_json["name"] != 'unknown' else None,
                    activity=Activity.objects.get(id=byte_to_json["activity"]),
                    total_time=float(byte_to_json["duration"].split('.')[1]),
                    start_time=byte_to_json["start_time"],
                    end_time=byte_to_json["end_time"],
                    date_time=datetime.now()
                )
                print("Forbidden activity")
            if msg.topic == self.fixed_place_people_count_ml_topic:
                print(msg.payload[1:-1])
            # print(msg.payload)

        client = mqtt.Client(client_id=self.client_id)
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(self.broker, self.port, 60)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_start()


# cv2.destroyAllWindows()
