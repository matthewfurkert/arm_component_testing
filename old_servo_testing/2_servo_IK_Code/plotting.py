import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, pi, acos, cos, tan, atan2, sin

from robot import x_loc, y_loc, q1, q2
from IK_function import l1, l2



# Defining the x and y locations for each joint
x2 = x_loc
x1 = x2 - l2*cos(q1+q2)
x0 = x1 - l1*cos(q1)
y2 = y_loc
y1 = y2 - l2*sin(q1+q2)
y0 = y1 - l1*sin(q1)


x_plot = np.array([x0, x1, x2])
y_plot = np.array([y0, y1, y2])

xpoints = np.array([x0, x1, x2])
ypoints = np.array([y0, y1, y2])

plt.plot(x_plot,y_plot, linewidth = '1')
plt.plot(xpoints, ypoints, 'o')

plt.title("Inverse Kinematics")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()