import time
import RPi.GPIO as GPIO

pumpPin=4
solenoidPin=26
count=0
from datetime import datetime
print(datetime.now())
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

while (count < 10000):
    count = count +1
    print(count)
    GPIO.output(16, GPIO.LOW)
    time.sleep(2)
    GPIO.output(4, GPIO.LOW)
    time.sleep(2)
    GPIO.output(26, GPIO.LOW)
    time.sleep(5)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(10)
    
    
    