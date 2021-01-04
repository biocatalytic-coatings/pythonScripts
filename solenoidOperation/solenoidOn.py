import time
import RPi.GPIO as GPIO

pumpPin=4
solenoidPin=26
count=0
from datetime import datetime
print(datetime.now())
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(myPin, GPIO.OUT)

while (count < 100):
    GPIO.output(PumpPin, GPIO.LOW)
    GPIO.output(SolenoidPin, GPIO.LOW)
    time.sleep(5)
    GPIO.output(SolenoidPin, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(PumpPin, GPIO.LOW)
    time.sleep(10)
    count = count +1
    