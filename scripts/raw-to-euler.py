#!/usr/bin/env python3
import os
import math

path = 'data/donnees_vol.txt.raw'
with open(path,'r') as ser:
    for line in ser:
        entries = line.split()
        mag   = [float(i) for i in entries[1:4]]
        accel = [float(i) for i in entries[5:8]]
        rot   = [float(i) for i in entries[9:12]]

        roll  = -math.atan2(accel[2], math.sqrt(math.pow(accel[0],2) + math.pow(accel[2],2)))
        pitch =  math.atan2(accel[0], math.sqrt(math.pow(accel[1],2) + math.pow(accel[2],2)))
        xh = (mag[0] * math.cos(pitch)) + \
             (mag[1] * math.sin(pitch) * math.sin(roll)) + \
             (mag[2] * math.sin(pitch) * math.cos(roll))

        yh   =  (-mag[1] * math.cos(roll)) + (mag[2]*math.sin(roll))

        yaw  =  math.atan2(yh, xh)
        if yaw<0:             
            yaw=yaw + (2*math.pi)

        print("!ANG:{:.8f},{:f},{:f}"
              .format(math.degrees(roll), math.degrees(pitch), math.degrees(yaw)))

