#!/usr/bin/python3

import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

PIN = 8


def init():
    GPIO.setwarnings(False)    # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
    # Set pin 8 to be an output pin and set initial value to low (off)
    GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)


def run():
    GPIO.output(PIN, GPIO.HIGH)  # Turn on
    sleep(1)                    # Sleep for 1 second
    GPIO.output(PIN, GPIO.LOW)  # Turn off
    sleep(1)                    # Sleep for 1 second


if __name__ == '__main__':
    print("Blink on GPIO=%s" % PIN)
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
