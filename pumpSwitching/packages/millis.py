import time
from datetime import datetime, timedelta
from __main__ import *

def __init__(self):
    pass

def timeDelay():
    dt=datetime.now()
    future_time=dt + timedelta(seconds=delayInterval)
    while (dt < future_time):
        dt=datetime.now()
