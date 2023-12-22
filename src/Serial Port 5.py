import serial
import struct
import time
import keyboard
import threading
import numpy

ser = serial.Serial(port="COM10", baudrate=57600, bytesize=8, timeout=0.01, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE)

rotate_percent = 0
lift_percent = 0
x = 0
y = 0
g = 0
c = 50


def data_check():
    global rotate_percent
    global lift_percent
    while True:
        if keyboard.is_pressed("right arrow"):
            rotate_percent += 10
        elif keyboard.is_pressed("left arrow"):
            rotate_percent -= 10
        elif keyboard.is_pressed("down arrow"):
            lift_percent += 10
        elif keyboard.is_pressed("up arrow"):
            lift_percent -= 10
        time.sleep(0.2)


i = 0
thr = threading.Thread(target=data_check, daemon=True)
thr.start()

while i != 5000:
    ser.write(struct.pack('<ccchhhh', b'\x5a', i.to_bytes(), b'\x08', x, y, g, c))
    time.sleep(1)
    read = struct.unpack('<cccih', ser.read(9))

    x = (int(rotate_percent - read[3] // 100)) // 10 * 500
    x = int(min(abs(x), 10_000) * numpy.sign(x))

    y = (int(lift_percent - read[4] // 100)) // 10 * 500
    y = int(min(abs(y), 10_000) * numpy.sign(y))
    # print(read)
    print(f'Поворот: target = {rotate_percent} %; now = {read[3] // 100} %; speed = {x}')
    print(f'Подъем: target = {lift_percent} %; now = {read[4] // 100} %; speed = {y}')
    i = i + 1
ser.close()
