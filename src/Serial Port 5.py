import serial
from struct import *
import time
import keyboard
import threading
import math

ser = serial.Serial(port="COM10", baudrate=57600, bytesize=8, timeout=0.01, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE)

rotate_position = 0
x = 0
y = 0
g = 0
c = 50


def data_check():
    global rotate_position
    while True:
        if keyboard.is_pressed("right arrow"):
            rotate_position = rotate_position + 10
        elif keyboard.is_pressed("left arrow"):
            rotate_position = rotate_position - 10
        time.sleep(0.2)


i = 0
thr = threading.Thread(target=data_check, daemon=True)
thr.start()

while i != 5000:
    ser.write(pack('<ccchhhh', b'\x5a', i.to_bytes(), b'\x08', x, y, g, c))
    time.sleep(1)
    read = unpack('<cccih', ser.read(9))
    x = int(rotate_position - read[3] / 100) // 2 * 1000
    x = int(min(math.abs(x), 10_000) * x / math.abs(x))
    print(x, read[3] // 100, rotate_position)
    i = i + 1
ser.close()
