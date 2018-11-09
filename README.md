# FBConsole

Framebuffer console class for MicroPython.

You can redirect REPL to any framebuffer devices.

## Usage

The example below duplicates REPL output to SSD1306 OLED connected to ESP32 (SDA=Pin22, SCL=Pin21).
```
def set_fb_console(fb, on=True):
    global theScreen
    from fbconsole import FBConsole
    import os
    if on:
        theScreen = FBConsole(fb)
        os.dupterm(theScreen)
    else:
        theScreen = os.dupterm(None)

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(21), sda=Pin(22), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

set_fb_console(oled)        # redirect REPL output to OLED
help()                      # and print something
set_fb_console(oled, False) # then disconnect OLED from REPL
theScreen.cls()             # and clear OLED screen
```

## Limitation

Only newlines and backspaces are supported as control charcters. All other control characters such as arrow keys are not supported. (see `_putc()` function)