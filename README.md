# HRV monitoring system demo - Pi side

This repository stores the codes of the Pi side for the heart rate variability monitoring system demo.

## Content

[Hardware introduction](README.md#hardware)

[Usage](README.md#usage)

## Hardware

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

## Connections

### Connect display to Pi

| LCD | BCM2835      | Board |
|-----|--------------|-------|
| VCC | 3.3V         | 3.3V  |
| GND | GND          | GND   |
| DIN | MOSI         | 19    |
| CLK | SCLK         | 23    |
| CS  | CE0          | 24    |
| DS  | 25           | 22    |
| RST | 27           | 13    |
| BL  | 18           | 12    |

<img src="Pictures/connections.jpg" width="600">

## Usage

Refer to this: [2inch_LCD_Module Workins with Raspberry Pi](https://www.waveshare.com/wiki/2inch_LCD_Module#Working_with_Raspberry_Pi)
