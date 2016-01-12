#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

channel = 24

def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	while GPIO.input(channel) == GPIO.LOW:
		time.sleep(1)
		#door is closed
		GPIO.cleanup()
		return 1
	GPIO.cleanup()
	return 0

if __name__=="__main__":
        print(main())
        

