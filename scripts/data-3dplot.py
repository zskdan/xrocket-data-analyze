#!/usr/bin/env python3
import os
import math
from time import sleep 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib

matplotlib.interactive(True)

path = 'data/donnees_vol.txt.integration'
with open(path,'r') as ser:
    coordt = []
    coordx = []
    coordy = []
    coordz = []
    fig = plt.figure()
    plt.title('xrocket 3d map')
    ax = Axes3D(fig)
    ax.set_xlim(600)
    ax.set_ylim(2000)
    ax.set_zlim(600)
    for line in ser:
        entries = line.split()
        t = float(entries[0][2:-1])
        x = float(entries[1][2:-1])
        y = float(entries[2][2:-1])
        z = float(entries[3][2:-1])
        coordx.append(x)
        coordy.append(y)
        coordz.append(z)
        ax.scatter(coordx, coordy, coordz)
        plt.draw()
        plt.pause(0.01)
        ax.cla()

    plt.draw()
    # show hight map in 3d
    #ax = fig.add_subplot(111, projection='3d')
    #ax = plt.axes(projection='3d')

    #ax.scatter(coordx, coordy, 0)

