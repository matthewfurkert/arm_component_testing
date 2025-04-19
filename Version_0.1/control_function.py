from gpiozero import AngularServo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()

from robot import q1_deg, q2_deg, q3_deg
from IK_function import degrees

servo2 = AngularServo(6, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo3 = AngularServo(13, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo4 = AngularServo(19, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

servo2.angle = 0
servo3.angle = 0
servo4.angle = 0
sleep(1)

servo2.angle = q1_deg
servo3.angle = q2_deg
servo4.angle = q3_deg
print("Angle of Servo 2:", servo2.angle)
print("Angle of Servo 3:", servo3.angle)
print("Angle of Servo 4:", servo4.angle)
sleep(2)


servo2.angle = 0
servo3.angle = 0
servo4.angle = 0
print("Servos Returning to Home position")
sleep(1)

servo2.value = None
servo3.value = None
servo4.value = None
