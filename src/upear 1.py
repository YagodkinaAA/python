import serial
from struct import *
import time
import keyboard
import threading

ser = serial.Serial(port="COM6", baudrate=460800, bytesize=8, timeout=0.01, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE)

id = 0
while id != 5000:
    read = ser.read(25)
    print(read)
    id += 1
ser.close()