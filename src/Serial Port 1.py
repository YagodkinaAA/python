import serial

ser = serial.Serial(port="COM5", baudrate=9600, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
ser.write("Hello!".encode('Ascii'))
ser.write("Прыгни вверх".encode('UTF-8'))
print(ser.readline().decode('UTF-8'))
ser.close()
