import time
import RPi.GPIO as GPIO

# myPin 4 = Pump
# myPin 16 = NO Solenoid
# myPin 26 = Pump Solenoid

myPin=16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(myPin, GPIO.OUT)

GPIO.output(myPin, GPIO.HIGH)
    