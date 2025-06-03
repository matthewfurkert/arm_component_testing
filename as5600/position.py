import smbus2
import time
import sys
import math

#=====================================================================
# Code to read AS5600.  9 lines of python is all it takes.
DEVICE_AS5600 = 0x36 # Default device I2C address
bus = smbus2.SMBus(3)

def ReadRawAngle(): # Read angle (0-360 represented as 0-4096)
  read_bytes = bus.read_i2c_block_data(DEVICE_AS5600, 0x0C, 2)
  return (read_bytes[0]<<8) | read_bytes[1]

def ReadMagnitude(): # Read magnetism magnitude
  read_bytes = bus.read_i2c_block_data(DEVICE_AS5600, 0x1B, 2)
  return (read_bytes[0]<<8) | read_bytes[1]

while True:
    raw_angle = ReadRawAngle()
    magnitude = ReadMagnitude()

    print("Raw angle: %4d"%(raw_angle), "m=%4d"%(magnitude), "%6.2f deg  "%(raw_angle*360.0/4096))
    time.sleep(1)