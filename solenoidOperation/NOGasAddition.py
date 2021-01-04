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

while (count < 10):
    count = count +1
    print(count)
    print(datetime.now())
    GPIO.output(16, GPIO.LOW)
    time.sleep(55)
    GPIO.output(16, GPIO.HIGH)
    print(datetime.now())
    time.sleep(300)
    
print("Auto dosing completed")
    
    
    