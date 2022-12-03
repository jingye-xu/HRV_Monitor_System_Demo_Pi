#!/usr/bin/python3
import os
import sys 
import time
import logging
import spidev as SPI
import serial
sys.path.append("..")
import LCD_2inch
from PIL import Image,ImageDraw,ImageFont
import numpy as np

# plot heart
def heart(xy, size, draw):
    x = np.linspace(-2, 2, 25)
    y1 = -np.sqrt(1 - (abs(x) - 1) ** 2)
    y2 = 3 * np.sqrt(1 - (abs(x) / 2) ** 0.5)

    poly1 = []
    poly2 = []

    for i in range(len(x)):
        poly1.append((x[i]*size + xy[0], (y1[i])*size + xy[1]))
        poly2.append((x[i]*size + xy[0], (y2[i])*size + xy[1]))

    draw.polygon(poly1, "red")
    draw.polygon(poly2, "red")

heart_size = np.append(np.linspace(6, 10, 5), np.linspace(10, 6, 5))
size_i = 0

# plot heart rate
def heart_trace(xy, heart, wide, high, draw, heart_t):

    heart_value = 0 if heart == None else float(heart)

    if heart_t == 0 or heart_value != heart_h[-1]:
        heart_h.append(heart_value)
    if len(heart_h) > 60:
        heart_h.pop(0)

    poly1 = []
    for i in range(len(heart_h)):
        poly1.append((xy[0] + i*wide/60, xy[1] + (240 - heart_h[i])*high/240))

    draw.line(poly1)

heart_h = []
heart_t = 0

# plot heart rate v
def heart_v_trace(xy, heart_v, wide, high, draw, heart_t):

    heart_v_value = 0 if heart_v == None else float(heart_v)

    if heart_t == 0 or heart_v_value != heart_v_h[-1]:
        heart_v_h.append(heart_v_value)
    if len(heart_v_h) > 60:
        heart_v_h.pop(0)

    poly1 = []
    for i in range(len(heart_v_h)):
        poly1.append((xy[0] + i*wide/60, xy[1] + (100 - heart_v_h[i])*high/100))

    draw.line(poly1)

heart_v_h = []

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)
try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    #disp = LCD_2inch.LCD_2inch(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_2inch.LCD_2inch()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    uart = serial.Serial("/dev/ttyACM1", 4800)
    power_mode = None
    HR = None
    HRV = None
    Time_HR = None
    Time_HRV = None

    while True:
        # Create blank image for drawing.
        image1 = Image.new("RGB", (disp.height, disp.width ), "BLACK")
        draw = ImageDraw.Draw(image1)
        Font = ImageFont.truetype("./times-new-roman.ttf",20)
        
        # check uart
        if uart.in_waiting >= 10:
            uart_data = uart.read(10)
            uart_data = uart_data.decode("utf-8", errors="ignore")
            if uart_data[0] == "s":
                power_mode = "start"
            elif uart_data[0] == "h":
                HR = uart_data[2:]
            elif uart_data[0] == "v":
                HRV = uart_data[2:]
            elif uart_data[0] == "t":
                Time_HR = uart_data[2:]
            elif uart_data[0] == "i":
                Time_HRV = uart_data[2:]
            elif uart_data[0] == "e":
                power_mode = "end"
                HR = None
                HRV = None
                Time_HR = None
                Time_HRV = None
        
        local_time = time.localtime(time.time())
        current_time = time.strftime("%m/%d/%Y %H:%M:%S", local_time)
        draw.text((5, 0), f'{current_time}', fill = "WHITE",font=Font)
        draw.text((5, 30), f'Mode: {power_mode if power_mode else "NA"}', fill = "WHITE",font=Font)
        draw.text((5, 60), f'HR: {HR if HR else "NA"}', fill = "WHITE",font=Font)
        draw.text((5, 90), f'time for HR: {Time_HR if Time_HR else "NA"}', fill = "WHITE",font=Font)
        draw.text((5, 120), f'HRV: {HRV if HRV else "NA"}', fill = "WHITE",font=Font)
        draw.text((5, 150), f'time for HRV: {Time_HRV if Time_HRV else "NA"}', fill = "WHITE",font=Font)
        
        
        heart_trace((20, 179), HR, 120, 60, draw, heart_t)
        heart_v_trace((180, 179), HRV, 120, 60, draw, heart_t)
        heart_t += 1
        heart_t %= 20

        heart((250, 50), heart_size[size_i], draw)
        size_i += 1
        size_i %= 10
        image1 = image1.rotate(180)
        disp.ShowImage(image1)
        time.sleep(0.05)
except KeyboardInterrupt:
    image1 = Image.new("RGB", (disp.height, disp.width ), "BLACK")
    draw = ImageDraw.Draw(image1)
    disp.ShowImage(image1)
    disp.module_exit()
    logging.info("quit:")
    exit()
