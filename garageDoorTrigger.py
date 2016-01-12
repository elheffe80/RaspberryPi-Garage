#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import garageDoorStatus

channel = 4

def main():
	if garageDoorStatus.main() == 1:
		print "opening garage door"
	else:
		print "closing garage door"
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(channel, GPIO.OUT)
	GPIO.output(channel,GPIO.LOW)
	time.sleep(1)
	GPIO.output(channel,GPIO.HIGH)
	GPIO.cleanup()

if __name__=="__main__":
	main()


