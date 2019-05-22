#!/usr/bin/env python
import time
import json
import paho.mqtt.client as mqtt
import uuid
import random

SERVER = "infmqtt.westeurope.azurecontainer.io"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def send(client, id):
    while True:
        time.sleep(5)
        data = {
            "DeviceId" : id,
            "Temp" : random.randrange(0,30),
            "Humidity" : random.randrange(500, 1000)
        }
        client.publish("iotro/mt/devices", json.dumps(data))
        print(".", end ="")

# Main
if __name__ == '__main__':
    try:
        client = mqtt.Client()
        client.on_connect = on_connect

        client.connect(SERVER, 1883, 60)
        client.loop_start()

        send(client, str(uuid.uuid4()))

    except Exception as e:
        print("Error occured: {0}".format(e.args))