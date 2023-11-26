import serial
import struct
import time
import keyboard
import threading
import numpy

ser = serial.Serial(port="COM10", baudrate=57600, bytesize=8, timeout=0.01, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE)

rotate_percent = 0
x = 0
y = 0
g = 0
c = 50


def data_check():
    global rotate_percent
    while True:
        if keyboard.is_pressed("right arrow"):
            rotate_percent += 10
        elif keyboard.is_pressed("left arrow"):
            rotate_percent -= 10
        time.sleep(0.2)


i = 0
thr = threading.Thread(target=data_check, daemon=True)
thr.start()

while i != 5000:
    ser.write(struct.pack('<ccchhhh', b'\x5a', i.to_bytes(), b'\x08', x, y, g, c))
    time.sleep(1)
    read = struct.unpack('<cccih', ser.read(9))

    rotate_angle = -(180 * rotate_percent / 100 - 90)
    x = (int(rotate_angle - read[3] / 100) // 2) * 1000
    x = int(min(abs(x), 10_000) * numpy.sign(x))
    print(x, read[3] // 100, rotate_angle)
    i = i + 1
ser.close()
