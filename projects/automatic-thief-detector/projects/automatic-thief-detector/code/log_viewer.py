# Simple Python serial monitor
import serial
ser = serial.Serial('COM3', 9600)  # Replace COM3 with your port
while True:
    print(ser.readline().decode().strip())
