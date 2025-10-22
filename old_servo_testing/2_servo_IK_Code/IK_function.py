from math import sqrt, pi, acos, cos, tan, atan2, sin

# Inverse kinematic equations
# The derivation of the equations are shown at:
# https://www.youtube.com/watch?v=RH3iAmMsolo&ab_channel=Woolfrey

# Define the length of each arm segment
l1 = 50
l2 = 50

# Calculating the servo angles
def angles(x,y):
    q2 = pi - acos((l1**2 + l2**2 - x**2 - y**2)/(2*l1*l2))
    q1 = atan2(y,x) - atan2((l2*sin(q2)),(l1 + l2*cos(q2)))
    return q1, q2

# Converting angles from radians to degrees
def degrees(angle):
  return angle * (180/pi)