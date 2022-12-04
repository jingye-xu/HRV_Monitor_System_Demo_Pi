#!/usr/bin/python3
import serial
from serialport import serialPort

uart = serial.Serial(serialPort, 9600)

while True:
    if uart.in_waiting:
        uart_data = uart.readline()
        uart_data = uart_data[:-1].decode("utf-8", errors="ignore")
        print(uart_data)
