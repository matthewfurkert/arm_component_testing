from math import sqrt, pi, acos, cos, tan, atan2, sin

# Inverse kinematic equations
# The derivation of the equations are shown at:
# https://www.youtube.com/watch?v=RH3iAmMsolo&ab_channel=Woolfrey

# Define the length of each arm segment
l1 = 50
l2 = 50
l3 = 30
gamma = pi/2

# Calculating the servo angles
def angles(x,y):
    q2 = pi - acos((l1**2 + l2**2 - (x-l3*cos(gamma))**2 - (y-l3*sin(gamma))**2)/(2*l1*l2))
    q1 = atan2((y-l3*sin(gamma)),(x-l3*cos(gamma))) - atan2((l2*sin(q2)),(l1 + l2*cos(q2)))
    q3 = gamma - (q1+q2)
    return q1, q2, q3

# Converting angles from radians to degrees
def degrees(angle):
  return angle * (180/pi)