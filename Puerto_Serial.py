import serial, time

arduino = serial.Serial("/dev/ttyACM0", 9600)

for i in range(0,5):
    time.sleep(1)
    arduino.write(b'1')
    print('OFF')
    time.sleep(1)
    arduino.write(b'0')
    print('ON')

arduino.close()