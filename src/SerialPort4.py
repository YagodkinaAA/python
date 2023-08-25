import serial
from struct import *
import time
import keyboard
import threading

ser = serial.Serial(port="COM5", baudrate=57600, bytesize=8, timeout=0.01, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE)

x = 0
y = 0
g = 0
c = 50
def data_check():
    global x
    global y
    global g
    while True:
        if keyboard.is_pressed("down arrow") and -20000 <= y < 20000:
            y = y + 5000
        elif keyboard.is_pressed("up arrow") and -20000 < y <= 20000:
            y = y - 5000
        elif keyboard.is_pressed("right arrow") and -20000 <= x < 20000:
            x = x + 5000
        elif keyboard.is_pressed("left arrow") and -20000 < x <= 20000:
            x = x - 5000
        elif keyboard.is_pressed('e') and -20000 <= g < 20000:
            g = g + 5000
        elif keyboard.is_pressed('q') and -20000 < g <= 20000:
            g = g - 5000
        #print(x, y, g)
        time.sleep(0.1)


id = 0
thr = threading.Thread(target=data_check, daemon=True)
thr.start()
while id != 5000:
    ser.write(pack('<ccchhhh', b'\x5a', id.to_bytes(), b'\x08', x, y, g, c))
    time.sleep(1)
    read = unpack('<ccchhhh', ser.read(11))
    print(read[3], read[4])
    id = id + 1
ser.close()
