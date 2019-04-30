#!/usr/bin/python

#Libraries
# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO 

PIN = 12

def button_down(channel):
	print("button pressed")

if __name__ == '__main__':
	GPIO.setwarnings(True)  	# Ignore warning for now
	GPIO.setmode(GPIO.BOARD) 	# Use physical pin numbering
	GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 	# Set pin to be an input pin and set initial value to be pulled low (off)


	GPIO.add_event_detect(PIN, GPIO.RISING, callback=button_down)

	message = input("Press enter to quit\n\n")

	GPIO.cleanup()

