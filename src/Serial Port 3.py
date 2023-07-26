import serial
from struct import *
import time
import keyboard

ser = serial.Serial(port="COM5", baudrate=57600, bytesize=8, timeout=0.01, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE)

# w - увеличить скорость подъема
# s - уменьшить скорость подъема
# d - увеличить скорость поворота
# a - уменьшить скорость поворота
# e - увеличить скорость сжатия
# q - уменьшить скорость сжатия
id = 0
x = 0
y = 0
g = 0
c = 50
while id != 50:
    if keyboard.is_pressed('w') and -20000 <= y < 20000:
        y = y + 5000
    elif keyboard.is_pressed('s') and -20000 < y <= 20000:
        y = y - 5000
    elif keyboard.is_pressed('d') and -20000 <= x < 20000:
        x = x + 5000
    elif keyboard.is_pressed('a') and -20000 < x <= 20000:
        x = x - 5000
    elif keyboard.is_pressed('e') and -20000 <= g < 20000:
        g = g + 5000
    elif keyboard.is_pressed('q') and -20000 < g <= 20000:
        g = g - 5000
    ser.write(pack('<ccchhhh', b'\x5a', id.to_bytes(), b'\x08', x, y, g, c))
    time.sleep(1)
    read = unpack('<ccchhhh', ser.read(11))
    print(read)
    id = id + 1
ser.close()
