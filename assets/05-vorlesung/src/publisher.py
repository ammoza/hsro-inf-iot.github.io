#!/usr/bin/env python

import time
import paho.mqtt.client as mqtt

SERVER = "infmqtt.westeurope.azurecontainer.io"  # iot.eclipse.org"
TOPIC = "iotro/led"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(SERVER, 1883, 60)

    client.loop_start()

    while True:
        time.sleep(5)
        client.publish(TOPIC, "blink")
