from math import sqrt, pi, acos, cos, tan, atan2, sin

#Arm length
L1 = 50
L2 = 50

#Position of end of arm
x2 = 00 
y2 = 90

# Position of base servo
x0 = 0
y0 = 0


def triangle1(x,y)->float:
  """ returns the value of the hypoteneuse """
  r = sqrt(x**2 + y**2) # mm
  gamma = atan2(y,x)
  return r, gamma

def triangle2(r)->float:
  """ Finds the value of angle Alpha"""
  return acos((L1**2 + L2**2 - r**2) / (2*L1*L2)) # alpha

def triangle3(alpha)->float:
  """ Returns the value of a2_sin_q2 """
  q2 = pi - alpha
  a2_sin_q2 = L2*sin(q2)
  
  return q2, a2_sin_q2 # Radians

def triangle4(q2)->float:
  """ Returns the angle Beta """
  return atan2(L2*sin(q2),L1+L2*cos(q2)) # beta

# Lets print out the values

r = triangle1(x2, y2)[0]
gamma = triangle1(x2, y2)[1]
alpha = triangle2(r)
q2 = triangle3(alpha)[0]
a2_sin_q2 = triangle3(alpha)[1]
beta = triangle4(q2)
# print("Triangle 1, r =",r,"mm")
# print("Triangle 2, alpha =",alpha,"rad")
# print("Triangle 3, q2 =",q2, "Radians")
# print("Triangle 3, a2_sin_q2 =",a2_sin_q2, "mm")
# print("Triangle 4, beta =",beta, "rad")

q1 = gamma - beta # Angle of servo 1 (rad)

def degrees(angle):
  # converts radians to degrees
  return angle * (180/pi)

alpha_degrees = degrees(alpha)
beta_degrees = degrees(beta)
gamma_degrees = degrees(gamma)
q1_degrees = degrees(q1)
q2_degrees = degrees(q2)

print("angle of servo1 (q1):", round((q1_degrees),2), "degrees")
print("angle of servo2 (q2):", round((q2_degrees),2), "degrees")

# Calculate the position of the elbow joint on the arm
x1 = x2 - L2*cos(q1+q2)
y1 = y2 - L2*sin(q1+q2)
print("x coordinate of elbow joint",round((x1),2))
print("x coordinate of elbow joint",round((y1),2))

import matplotlib.pyplot as plt
import numpy as np

x_plot = np.array([x0, x1, x2])
y_plot = np.array([y0, y1, y2])

xpoints = np.array([x0, x1, x2])
ypoints = np.array([y0, y1, y2])

# plt.plot(x1, y1)

plt.plot(x_plot,y_plot, linewidth = '1')
plt.plot(xpoints, ypoints, 'o')

plt.title("Inverse Kinematics")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()