#port
#baudrate
#bytesize
#timeout
#stopbits
import time
import serial
import keyboard

ser = serial.Serial(port="COM5", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

while True:
    #ser.write("This is the message".encode('Ascii'))
    ser.write("This is the message\r\n".encode('Ascii'))
    #receive = ser.read()
    receive = ser.readline()
    print(receive.decode('Ascii'))
    time.sleep(1)
    if keyboard.is_pressed('q'):
        print("User need to Quit the application")
        break

ser.close()
