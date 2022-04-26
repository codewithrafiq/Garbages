from django.conf import settings

# from project import settings

if settings.MQTT == True:
    from utils.client import MQTTClient
    mqtt_client = MQTTClient()
    mqtt_client.run()