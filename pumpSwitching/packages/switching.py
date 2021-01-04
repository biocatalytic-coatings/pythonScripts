import time
import RPi.GPIO as GPIO
from __main__ import *
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(myPin, GPIO.OUT)

def __init__(self):
    pass
    
def switchON():
    GPIO.output(myPin, GPIO.LOW)
    
def switchOFF():
    GPIO.output(myPin, GPIO.HIGH)