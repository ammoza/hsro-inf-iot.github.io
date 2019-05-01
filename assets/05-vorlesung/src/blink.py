#!/usr/bin/python3

import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

GPIO = 18


def init():
    GPIO.setwarnings(False)    # Ignore warning for now
    GPIO.setmode(GPIO.BCM)   # Use physical pin numbering
    # Set pin 8 to be an output pin and set initial value to low (off)
    GPIO.setup(GPIO, GPIO.OUT, initial=GPIO.LOW)


def run():
    GPIO.output(GPIO, GPIO.HIGH)  # Turn on
    sleep(1)                    # Sleep for 1 second
    GPIO.output(GPIO, GPIO.LOW)  # Turn off
    sleep(1)                    # Sleep for 1 second


if __name__ == '__main__':
    print("Blink on GPIO=%s" % GPIO)
    init()
    try:
        # Run forever
        while True:
            run()
            print(".", end="", flush=True)

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("stopped by User")
    GPIO.cleanup()
