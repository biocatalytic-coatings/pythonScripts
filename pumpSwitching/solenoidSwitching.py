import time
import RPi.GPIO as GPIO
from __main__ import *
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(myPin, GPIO.OUT)