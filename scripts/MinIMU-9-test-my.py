#!/usr/bin/env python3

from vpython import *
import string
import math
from time import sleep
from time import time

grad2rad = 3.141592/180.0
path = 'data/donnees_vol.txt.euler'
ser = open(path,'r')

roll=0
pitch=0
yaw=0

scene  = canvas(title="Pololu MinIMU-9 + Arduino AHRS -Scene1", x=0, y=0, width=800, height=600,center=vector(0,0,0), background=vector(0,0,0))
scene2 = canvas(title='<br>Pololu MinIMU-9 + Arduino AHRS -Scene2', x=0, y=0, width=800, height=600,center=vector(0,0,0), background=vector(0,0,0))

scene.forward = vector(1,0,-0.25)
scene.up=vector(0,0,1)

####################################################################################
# Main scene
####################################################################################
# Main scene objects
scene.select()
# Reference axis (x,y,z)
arrow(color=color.green,axis=vector(1,0,0), shaftwidth=0.02, fixedwidth=1)
arrow(color=color.green,axis=vector(0,-1,0), shaftwidth=0.02 , fixedwidth=1)
arrow(color=color.green,axis=vector(0,0,-1), shaftwidth=0.02, fixedwidth=1)
# labels
label(pos=vector(0,0,0.8),text="Pololu MinIMU-9 + Arduino AHRS",box=0,opacity=0)
label(pos=vector(1,0,0),text="X",box=0,opacity=0)
label(pos=vector(0,-1,0),text="Y",box=0,opacity=0)
label(pos=vector(0,0,-1),text="Z",box=0,opacity=0)
# IMU object
platform = box(length=1, height=0.05, width=1, color=color.blue)
p_line = box(length=1,height=0.08,width=0.1,color=color.yellow)
plat_arrow = arrow(color=color.green,axis=vector(1,0,0), shaftwidth=0.06, fixedwidth=1)

ts = label(pos=vector(0,0,0.7),text="-:-:-",box=0,opacity=0)
####################################################################################
# Main scene objects
####################################################################################
scene2.select()

#Roll, Pitch, Yaw
cil_roll = cylinder(pos=vector(-0.6,0,0),axis=vector(0.2,0,0),radius=0.01,color=color.red)
cil_roll2 = cylinder(pos=vector(-0.6,0,0),axis=vector(-0.2,0,0),radius=0.01,color=color.red)
cil_pitch = cylinder(pos=vector(0.0,0,0),axis=vector(0.2,0,0),radius=0.01,color=color.green)
cil_pitch2 = cylinder(pos=vector(0.0,0,0),axis=vector(-0.2,0,0),radius=0.01,color=color.green)
arrow_course = arrow(pos=vector(0.6,0,0),color=color.cyan,axis=vector(-0.2,0,0), shaftwidth=0.02, fixedwidth=1)

#Roll,Pitch,Yaw labels
label(pos=vector(-0.6,0.3,0),text="Roll",box=0,opacity=0)
label(pos=vector(0.0,0.3,0),text="Pitch",box=0,opacity=0)
label(pos=vector(0.55,0.3,0),text="Yaw",box=0,opacity=0)
label(pos=vector(0.6,0.22,0),text="N",box=0,opacity=0,color=color.yellow)
label(pos=vector(0.6,-0.22,0),text="S",box=0,opacity=0,color=color.yellow)
label(pos=vector(0.38,0,0),text="W",box=0,opacity=0,color=color.yellow)
label(pos=vector(0.82,0,0),text="E",box=0,opacity=0,color=color.yellow)
label(pos=vector(0.75,0.15,0),height=7,text="NE",box=0,color=color.yellow)
label(pos=vector(0.45,0.15,0),height=7,text="NW",box=0,color=color.yellow)
label(pos=vector(0.75,-0.15,0),height=7,text="SE",box=0,color=color.yellow)
label(pos=vector(0.45,-0.15,0),height=7,text="SW",box=0,color=color.yellow)

L1 = label(pos=vector(-0.6,0.22,0),text="-",box=0,opacity=0)
L2 = label(pos=vector(0.0,0.22,0),text="-",box=0,opacity=0)
L3 = label(pos=vector(0.7,0.3,0),text="-",box=0,opacity=0)

n = 0
for line in ser:
    sleep(0.1)
    if line.find("!ANG:") != -1:          # filter out incomplete (invalid) lines
        line = line.replace("!ANG:","")   # Delete "!ANG:"
        #print(line)
        words = line.split(",")    # Fields split
        if len(words) > 2:
            try:
                roll = float(words[0])*grad2rad
                pitch = float(words[1])*grad2rad
                yaw = float(words[2])*grad2rad
            except:
                print("Invalid line")

            n += 1
            ts.text = str(n)
            axis=vector(cos(pitch)*cos(yaw),-cos(pitch)*sin(yaw),sin(pitch)) 
            up=vector(sin(roll)*sin(yaw)+cos(roll)*sin(pitch)*cos(yaw),sin(roll)*cos(yaw)-cos(roll)*sin(pitch)*sin(yaw),-cos(roll)*cos(pitch))
            platform.axis=axis
            platform.up=up
            platform.length=1.0
            platform.width=0.65
            plat_arrow.axis=axis
            plat_arrow.up=up
            plat_arrow.length=0.8
            p_line.axis=axis
            p_line.up=up
            cil_roll.axis=vector(0.2*cos(roll),0.2*sin(roll),0)
            cil_roll2.axis=vector(-0.2*cos(roll),-0.2*sin(roll),0)
            cil_pitch.axis=vector(0.2*cos(pitch),0.2*sin(pitch),0)
            cil_pitch2.axis=vector(-0.2*cos(pitch),-0.2*sin(pitch),0)
            arrow_course.axis=vector(0.2*sin(yaw),0.2*cos(yaw),0)
            L1.text = str(float(words[0]))
            L2.text = str(float(words[1]))
            L3.text = str(float(words[2]))        
    else:
            print("Not found")

print("EOF")
ser.close()
