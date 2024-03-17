from gpiozero import AngularServo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()

from robot import q1_deg, q2_deg, q3_deg
from IK_function import degrees

servo1 = AngularServo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo2 = AngularServo(27, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo3 = AngularServo(22, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

servo1.angle = 0
servo2.angle = 0
servo3.angle = 0
sleep(1)

servo1.angle = q1_deg
servo2.angle = q2_deg
servo3.angle = q3_deg
print("Angle of Servo 1:", servo1.angle)
print("Angle of Servo 2:", servo2.angle)
print("Angle of Servo 3:", servo3.angle)
sleep(2)


servo1.angle = 0
servo2.angle = 0
servo3.angle = 0
print("Servos Returning to Home position")
sleep(1)

servo1.value = None
servo2.value = None
servo3.value = None
# %%
