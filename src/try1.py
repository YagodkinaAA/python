import serial
from struct import *
import time

ser = serial.Serial(port="COM5", baudrate=57600, bytesize=8, timeout=0.01, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE)
id = 0
list = []
while id != 5:
    x = 00
    y = 0
    g = 20000
    c = 50
    ser.write(pack('<ccchhhh', b'\x5a', id.to_bytes(), b'\x08', x, y, g, c))
    time.sleep(1)
    # ser.write("Прыгни вверх".encode('UTF-8'))
    read = unpack('<ccchhhh', ser.read(11))
    list.append(read)
    # print(read[3], read[4])
    # print(ser.read(size=10).decode('UTF-8'))
    id = id + 1
print(list)
print(chr(65))
a = 60
b = 18
print(a & b)

ser.close()
