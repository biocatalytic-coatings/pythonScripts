import time
from datetime import datetime, timedelta
import RPi.GPIO as GPIO


solenoidPin=26
    
#  Define and load variable from main program.
#  additionCycles=
#  dosingTime
#  stabilisationTime=

cycles=0
from datetime import datetime
print(datetime.now())
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

start1=datetime.now()
while (cycles < 10):
    cycles = cycles +1
    print(cycles)
    finish = datetime.now() + timedelta(milliseconds=55000)
    GPIO.output(16, GPIO.LOW)
    
    while (datetime.now() < finish):
        continue

    finish = datetime.now() + timedelta(milliseconds=300000)
    GPIO.output(16, GPIO.HIGH)
    
    while (datetime.now() < finish):
        continue
    
    continue

print(datetime.now() - start1)