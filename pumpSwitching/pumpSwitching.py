import time
from datetime import datetime
print(datetime.now())
myPin=3
delayInterval=60
from packages import switching
from packages import millis

while True:

    switching.switchON()
    start_time=datetime.now()
    print(start_time)
    millis.timeDelay()

    switching.switchOFF()
    start_time=datetime.now()
    print(start_time)
    millis.timeDelay()

