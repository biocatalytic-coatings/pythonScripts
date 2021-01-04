import time
from datetime import datetime
timeNow=datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')

myPin=4
delayInterval=60
from packages import switching
from packages import millis
print("Pump off...",timeNow)
switching.switchOFF()