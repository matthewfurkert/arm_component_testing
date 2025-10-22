# Script for controlling the robotic arm
from IK_function import angles, degrees

x_loc = 70
y_loc =100


q1 = angles(x_loc,y_loc)[0]
q2 = angles(x_loc,y_loc)[1]
q3 = angles(x_loc,y_loc)[2]

q1_deg = degrees(q1)
q2_deg = degrees(q2)
q3_deg = degrees(q3)

print("Servo Angle (q1_A):", round((q1_deg),2), "degrees")
print("Servo Angle (q2_A):", round((q2_deg),2), "degrees")
print("Servo Angle (q3_A):", round((q3_deg),2), "degrees")