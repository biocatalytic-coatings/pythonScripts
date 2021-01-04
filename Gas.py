#
#   Program name    |   Gas.py
#   Written by      |   Steven Owen
#   Date            |   June 2020
#   Version         |   1.1
#
#   Description     |   A program to read electrode responses from an Alphasense AFE through the
#                       South Coast SCience DFE via a Raspberry Pi3.
#
#   Comments        |   This version is functionally correctly.  Try loops with error handling
#                       for connection errors have been included.
#                       
#                       Version 1.1 : This is an update to Gas53.py which has been used for the
#                       previous work on the Raspberry Pi3.  In the new experiment setup, we are
#                       using a Raspberry Pi4 and including a air pump system to allow for pulse
#                       sampling.  Additionally, climate reading are measured by a separate
#                       python script and publishing to Thingsboard is also handled by another
#                       separate python script.  This script now averages the electrode readings
#                       and returns them to the calling program.

#   Import necessary libraries.
import time
from datetime import datetime, timedelta
import socket
import sys
import os
import re
#import commands
import ADS1x15
#from Adafruit_SHT31 import *
#import paho.mqtt.client as mqtt
#import json

loops = int(sys.argv[1])

# Create ADS1115 ADC (16-bit) instances.
adcFE = ADS1x15.ADS1115(address=0x48, busnum=1) # FE prefix = Forty Eight (Auxilliary Electrode)
adcFN = ADS1x15.ADS1115(address=0x49, busnum=1) # FN prefix = Forty Nine  (Working Electrode)
GAIN=8

# Now we will create a loop to average the electrode readings. The number of samples to average is
# set in the calling program and passed to this script as sys.argv[1]. We take electrode readings at
# 1Hz. There is a delay that uses the millis approach for each cycle.

count = 0
FEvalues = [0]*4
FNvalues = [0]*4
#loops = 5
startGasAnalysis=datetime.now()
print("Starting gas analysis....",startGasAnalysis)
while (count < loops):
        futureTime = datetime.now() + timedelta(milliseconds=1000)
        count = count +1
        FEvalues[3] = FEvalues[3]+adcFE.read_adc(3, gain=GAIN)
        FNvalues[3] = FNvalues[3]+adcFN.read_adc(3, gain=GAIN)
        FEvalues[2] = FEvalues[2]+adcFE.read_adc(2, gain=GAIN)
        FNvalues[2] = FNvalues[2]+adcFN.read_adc(2, gain=GAIN)
        dt=datetime.now()
        while (dt < futureTime):
                dt=datetime.now()

NO2_WE=round((FNvalues[3]*4.096/loops)/(32768*GAIN),5)
NO2_AE=round((FEvalues[3]*4.096/loops)/(32768*GAIN),5)
NO_WE=round((FNvalues[2]*4.096/loops)/(32768*GAIN),5)
NO_AE=round((FEvalues[2]*4.096/loops)/(32768*GAIN),5)

finishedGasAnalysis=datetime.now()
print("Finished gas analysis....",finishedGasAnalysis)
duration=finishedGasAnalysis-startGasAnalysis
print("Duration (seconds)....",duration)

print(NO_WE)
print(NO_AE)
print(NO2_WE)
print(NO2_AE)






    
