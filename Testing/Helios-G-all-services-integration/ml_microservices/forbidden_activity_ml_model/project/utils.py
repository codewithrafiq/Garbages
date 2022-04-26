from http import client
import json
from vidgear.gears import NetGear
from decouple import config
from paho.mqtt import client as mqtt_client
import cv2
# import logging
# import logging
# import logging.handlers
from datetime import datetime
from project.ml.merge import MERGE


# print("id------>")
merge = MERGE()

# # print("merge---id------>",id(merge))

# LOG_FILENAME = 'mlEngineEntry.log'

# logging.basicConfig(filename=LOG_FILENAME, filemode='a',
#                     format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# # Creating an object
# my_logger = logging.getLogger()

# # Setting the threshold of logger to DEBUG
# my_logger.setLevel(logging.DEBUG)

# handler = logging.handlers.RotatingFileHandler(
#     LOG_FILENAME, maxBytes=20000000, backupCount=5)

# my_logger.addHandler(handler)


# # # broker = config("MQTT_IP")
# # # port = config("MQTT_PORT", cast=int)


broker = '192.168.1.231'
port = 1883
topic = "forbidden_activity_ml_topic"
client_id = "forbidden_activity_ml_id"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id=client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def videoFeed():
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
        address=config("CLIENT_IP", cast=str),

        port=config("CLIENT_PORT", cast=int),

        protocol="tcp",

        pattern=2,

        receive_mode=True,

        logging=True,

        **options

    )

    # loop over
    while True:
        try:
            # print(datetime.now())
            # recei`ve frames from network
            frame = netGear_client.recv()
            # print(frame.shape)
            cv2.imshow("frame", frame)
            cv2.waitKey(1)
            data = merge.main(frame)
            print("netGear_client----data-------------_-_-_-_-", data)
            # print("netGear_client----activity-------------_-_-_-_-", data['activity'])
            # print("netGear_client----name-------------_-_-_-_-", data['name'])
            # print("netGear_client----duration-------------_-_-_-_-", data['duration'])
            # print("netGear_client----start_time-------------_-_-_-_-", data['start_time'])
            # print("netGear_client----end_time-------------_-_-_-_-", data['end_time'])

            final_data = {
                "activity": f"{data['activity']}",
                "name": f"{data['name']}",
                "duration": f"{data['duration']}",
                "start_time": f"{data['start_time']}",
                "end_time": f"{data['end_time']}"
            }
            print("final_data---->", final_data)

            '''
             {'activity': 2, 'name': 'unknown', 'duration': datetime.timedelta(microseconds=375804), 
             'start_time': datetime.datetime(2022, 3, 16, 0, 31, 8, 776505), 'end_time': datetime.datetime(2022, 3, 16, 0, 31, 9, 152309)}
            '''


            client.publish(topic, bytes(json.dumps(final_data), encoding='utf-8'))

            # client.publish(topic, "hello")


            # forbidden_activity = data["forbidden_activity"]
            # side_talk = data["side_talk"]
            # absence = data["absence"]

            # print("forbidden_activity-------->",forbidden_activity)
            # print("side_talk-------->",side_talk)
            # print("absence-------->",absence)

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
            # client.publish(topic, f"forbidden_activity_ml_topic {datetime.now()}")
        except Exception as e:
            # my_logger.debug(f"{e}")
            with open("error.txt", "a") as f:
                f.write(f"{e}")

    cv2.destroyAllWindows()
    # # safely close client
    client.close()
