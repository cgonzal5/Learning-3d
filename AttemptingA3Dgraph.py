# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:58:17 2019

@author: Clayton Gonzales
"""
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
#it shows numpy is needed in most variations of this but according to the notification provided numpy is not being used.

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data (0.05)
ax.plot_wireframe(x,y,z, rstride=4, cstride=4)

plt.show