import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
interval = 5

def do_switching():
    # Configuring the outputs this
    # way ensures that the light on
    # the relay is switched on when
    # the circuit is energised providing
    # a visual reference.
    GPIO.output(3, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(3, GPIO.HIGH)
    time.sleep(interval)
    
while True:
    do_switching()