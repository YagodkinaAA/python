import serial
from struct import *
import time

ser = serial.Serial(port="COM10", baudrate=57600, bytesize=8, timeout=0.01, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE)
id = 0
while id != 100:
    x = 00
    y = 0
    g = 20000
    c = 50
    ser.write(pack('<ccchhhh', b'\x5a', id.to_bytes(), b'\x08', x, y, g, c))
    time.sleep(1)
    #ser.write("Прыгни вверх".encode('UTF-8'))
    read = unpack('<cccih', ser.read(9))
    print(read[3], read[4])
    # print(ser.read(size=10).decode('UTF-8'))
    id = id + 1


ser.close()
