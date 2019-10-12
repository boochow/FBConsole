# FBConsole

Framebuffer console class for MicroPython.

You can redirect REPL to any framebuffer devices.

## Usage

The example below duplicates REPL output to SSD1306 OLED connected to ESP32 via I2C(SDA=Pin22, SCL=Pin21).
```
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(21), sda=Pin(22), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

from fbconsole import FBConsole
import os
scr = FBConsole(oled)
os.dupterm(scr)        # redirect REPL output to OLED
help()                 # and print something
os.dupterm(None)       # then disconnect OLED from REPL
scr.cls()              # and clear OLED screen
```
![top-page](https://raw.githubusercontent.com/boochow/FBConsole/images/dupterm-oled.gif)

## ST7735 Wrapper

ST7735fb.py is a wrapper class to use FBConsole with ST7735-based small TFT LCD.
It provides some of FrameBuffer class APIs necessary to use FBConsole.
Use this with [ST7735 driver for MicroPython](https://github.com/boochow/MicroPython-ST7735).
Only LCDs with ST7735S(and maybe ST7735R) are supported because this wrapper class requires hardware scroll functionality.

## petme128 font

petme128.py is a font converted from ``petme128-font.c`` used in the framebuf class of MicroPython.

## ST7735fb usage

```
# This example is for ESP32 + ST7735S TFT LCD
from ST7735 import TFT
from machine import SPI,Pin
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft=TFT(spi,16,17,18)
tft.initb2()
tft.rgb(True)

# Assign 2 pixels for fixed and invisible area
# (ST7735S frame buffer vertical size is 162 pixels)
tft.setvscroll(1, 1)

# Wrapper object for FBConsole
from ST7735fb import TFTfb
from petme128 import petme128
fb = TFTfb(tft, petme128)

# redirect MicroPython terminal to ST7735
from fbconsole import FBConsole
scr = FBConsole(fb, TFT.BLACK, TFT.WHITE)

import os
os.dupterm(scr) 
```
![top-page](https://raw.githubusercontent.com/boochow/FBConsole/images/st7735-dupterm.jpg)
