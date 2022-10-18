# HRV monitoring system demo - Pi side

This repository stores the codes of the Pi side for the heart rate variability monitoring system demo.

## Parts

### Display

![](Pictures/2InchDisplay.jpg)

This is a general LCD display Module, IPS screen, 2inch diagonal, 240×320 resolution, with embedded controller, communicating via SPI interface.
[Product link](https://www.waveshare.com/2inch-lcd-module.htm)

#### Specifications

* Driver: ST7789
* Interface: SPI
* Display color: RGB, 262K color
* Resolution: 240×320
* Backlight: LED
* Operating voltage: 3.3V/5V

#### Interfaces

| SYMBOL |                       DESCRIPTION                       |
|:------:|:-------------------------------------------------------:|
|   VCC  |                  Power (3.3V/5V input)                  |
|   GND  |                          Ground                         |
|   DIN  |                      SPI data input                     |
|   CLK  |                     SPI clock input                     |
|   CS   |                Chip selection, low active               |
|   DC   | Data/Command selection (high for data, low for command) |
|   RST  |                    Reset, low active                    |
|   BL   |                        Backlight                        |

#### Dimensions

<img src="Pictures/displaySize.jpg" width="500">

### PPG Sensor

[Product Link](https://www.amazon.com/gp/product/B076LQKQFF/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)

### MSP430FR5994

### Raspberry Pi 4B

