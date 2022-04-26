import base64
from ctypes import cast
from traceback import print_tb
from vidgear.gears import NetGear
from decouple import config
from paho.mqtt import client as mqtt_client
import json
import cv2
import logging
import logging
import logging.handlers
from decouple import config
from datetime import datetime
from project.ml_model.count_api import COUNTING


count = COUNTING()

LOG_FILENAME = 'mlEngineEntry4.log'

logging.basicConfig(filename=LOG_FILENAME, filemode='a',
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# Creating an object
my_logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=20000000, backupCount=5)

my_logger.addHandler(handler)



broker = config("MQTT_IP", cast=str)
port = config("MQTT_PORT", cast=int)
topic = "worker_count_ml_topic"
client_id = "worker_count_ml_id"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id=client_id)
    client.on_connect = on_connect
    client.connect(broker, port,keepalive=0)
    return client


class VideoFeed:

    def start(self):
        '''
        Initialize a NetGear client at given IP address and port, 
        receive frames from network, 
        count the number of people in the frame, 
        and show the output frame.


        :return: None
        '''
        client = connect_mqtt()
        # define various tweak flags

        options = {"flag": 0, "copy": False, "track": False}

        # Define Netgear Client at given IP address and define parameters
        # !!! change following IP address '192.168.x.xxx' with yours !!!
        netGear_client = NetGear(

            # address=str(socket.gethostbyname(socket.gethostname())),
            address=config("CLIENT_IP"),

            port=config("CLIENT_PORT"),

            protocol="tcp",

            pattern=2,

            receive_mode=True,

            logging=True,

            **options

        )

        # loop over
        while True:
            try:

                frame = netGear_client.recv()
                # frame = cv2.resize(frame, (800, 720))
                # frame = cv2.flip(frame, 1)
                # frame = cv2.rotate(frame, cv2.ROTATE_360_CLOCKWISE)
                # cv2.imshow("Frame", frame)
                # cv2.waitKey(1)
                # entry_gate = count.entry_count(frame)
                # my_logger.info(entry_gate)

                
                # print("entry_gate------->",entry_gate)

                # if int(entry_gate["enter"]) >0 or int(entry_gate["exit"]) >0:
                #     client.publish(topic, bytes(json.dumps(entry_gate), encoding="utf-8"))
                client.publish(topic, f"Im Comming {datetime.now()}")





                # recei`ve frames from network
                # frame = netGear_client.recv()
                # _, buffer = cv2.imencode('.jpg', frame)
                # frame = base64.b64encode(buffer).decode('utf8')
                # print(frame)
                # cv2.imshow("Frame", frame)
                # cv2.waitKey(1)
                # data = cv2.imencode('.jpg', frame)[1].tobytes()
                # client.publish(topic, json.dumps({"img": data}))
                # client.publish(topic, 'json.dumps({"img": data})')

                # client.publish(topic, json.dumps({"frame": base64.b64encode(frame).decode("utf-8")}))
                # frame_to_base64 = base64.b64encode(frame).decode("utf-8")
                # client.publish(topic, frame_to_base64)
                
                
                # client.publish(topic, json.dumps(entry_gate))
            except Exception as e:
                my_logger.debug(f"{e}")

        cv2.destroyAllWindows()
        # # safely close client
        client.close()
