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


class Controller:
    def __init__(self):
        self.target = 0
        self.now = 0
        self.speed = 0

    def put(self, read, target):
        self.target = target
        self.speed = (int(target - read // 100)) // 10 * 500
        self.speed = int(min(abs(self.speed), 10_000) * numpy.sign(self.speed))
        self.now = read // 100


def data_check():
    global rotate_percent
    global lift_percent
    while True:
        if keyboard.is_pressed("left arrow"):
            rotate_percent += 10
        elif keyboard.is_pressed("right arrow"):
            rotate_percent -= 10
        elif keyboard.is_pressed("down arrow"):
            lift_percent += 10
        elif keyboard.is_pressed("up arrow"):
            lift_percent -= 10
        time.sleep(0.2)


i = 0
thr = threading.Thread(target=data_check, daemon=True)
thr.start()
rotate = Controller()
catch = Controller()
while i != 5000:
    x = rotate.speed
    y = catch.speed
    ser.write(struct.pack('<ccchhhh', b'\x5a', i.to_bytes(), b'\x08', x, y, g, c))
    time.sleep(1)
    read = struct.unpack('<cccih', ser.read(9))

    rotate.put(read[3], rotate_percent)
    print(f'Поворот: {rotate.__dict__}')

    catch.put(read[4], lift_percent)
    print(f'Подъем: {catch.__dict__}')

    i = i + 1
ser.close()
