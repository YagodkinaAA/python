import serial
from struct import *

ser = serial.Serial(port="COM5", baudrate=57600, bytesize=8, timeout=0.01, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE)

id = 0
x = 20000
y = 0
g = 0
c = 50
ser.write(pack('<ccchhhh', b'\x5a', id.to_bytes(), b'\x08', x, y, g, c))
#ser.write("Прыгни вверх".encode('UTF-8'))
print(ser.readline().hex())
# print(ser.read(size=10).decode('UTF-8'))

ser.close()
