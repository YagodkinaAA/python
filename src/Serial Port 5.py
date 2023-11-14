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
        if keyboard.is_pressed("right arrow") and -20000 <= x < 20000:
            rotate_position = rotate_position + 10

        elif keyboard.is_pressed("left arrow") and -20000 < x <= 20000:
            rotate_position = rotate_position - 10
        time.sleep(0.2)


def sign(num):
    if num < 0:
        return -1
    else:
        return 1


i = 0
thr = threading.Thread(target=data_check, daemon=True)
thr.start()

while i != 5000:
    ser.write(pack('<ccchhhh', b'\x5a', i.to_bytes(), b'\x08', x, y, g, c))
    time.sleep(1)
    read = unpack('<cccih', ser.read(9))
    x = int(rotate_position - read[3] // 1000) * 2 * 200
    x = int(min(math.fabs(x), 10_000) * sign(x))
    print(x, read[3], rotate_position)
    i = i + 1
ser.close()
