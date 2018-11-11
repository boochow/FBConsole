# FBConsole

Framebuffer console class for MicroPython.

You can redirect REPL to any framebuffer devices.

## Usage

The example below duplicates REPL output to SSD1306 OLED connected to ESP32 (SDA=Pin22, SCL=Pin21).
```
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(21), sda=Pin(22), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

from fbconsole import FBConsole
import os
scr = FBConsole(fb)
os.dupterm(scr)        # redirect REPL output to OLED
help()                 # and print something
os.dupterm(None)       # then disconnect OLED from REPL
scr.cls()              # and clear OLED screen
```

![top-page](https://raw.githubusercontent.com/boochow/FBConsole/images/dupterm-oled.jpg)