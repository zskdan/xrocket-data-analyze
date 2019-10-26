#!/usr/bin/env python3
import os
import math
import matplotlib.pyplot as plt

path = 'data/donnees_vol.txt.raw'
with open(path,'r') as ser:
    accelx = []
    accely = []
    accelz = []
    accelp = []
    for line in ser:
        entries = line.split()
        mag   = [float(i) for i in entries[1:4]]
        accel = [float(i) for i in entries[5:8]]
        rot   = [float(i) for i in entries[9:12]]
        accelx.append(accel[0])
        accely.append(accel[1])
        accelz.append(accel[2])
        accelp.append(math.sqrt((accel[2]*accel[2])+(accel[1]*accel[1])+(accel[0]*accel[0])))

    plt.plot(accelp)
    #plt.plot(accely)
    #plt.plot(accelz)
    plt.show()

