import keyboard
import serial


ser = serial.Serial(port="COM5", baudrate=57600, bytesize=8, timeout=0.01, parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE)
while True:

    if keyboard.is_pressed('w'):
        print('Good Luck')
        break
    elif keyboard.is_pressed('s'):
        print('Good Luck1')
        break
    elif keyboard.is_pressed('d'):
        print('Good Luck2')
        break
    elif keyboard.is_pressed('a'):
        print('Good Luck3')
        break
# ser.write("Прыгни вверх".encode('UTF-8'))
# print(ser.read(size=10).decode('UTF-8'))
ser.close()