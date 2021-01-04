import time
from datetime import datetime, timedelta

interval=1

start_time=datetime.now()
future_time=start_time + timedelta(seconds=60)

dt=datetime.now()
print("Started @",dt)
while (dt < future_time):
    #time.sleep(interval)
    #print("Millis = ",dt)
    dt=datetime.now()
    
print ("Finished @", datetime.now())
