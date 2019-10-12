# ST7735S driver wrapper for FBConsole
# ST7735 driver: https://github.com/boochow/MicroPython-ST7735
# FBConsole: https://github.com/boochow/FBConsole

class TFTfb(object):
    def __init__(self, tft, font):
        self.height = 160
        self.width = 128
        self.tft = tft
        self.font = font
        tft.setvscroll(tft.tfa, tft.bfa)
        tft.fill(0)
        tft.vscroll(0)
        self.voffset = 0

    def _abs2tft(self, v) :
        ''' convert screen y coord to LCD address'''
        return (self.voffset + v) % self.height

    def fill(self, color) :
        self.tft.fill(color)

    def fill_rect(self, x, y, w, h, color) :
        top = self._abs2tft(y)
        bottom = self._abs2tft(y + h)
        if (bottom > top):
            self.tft.fillrect((x, top), (w, h), color)
        else:
            self.tft.fillrect((x, top), (w, self.height - top), color)
            self.tft.fillrect((x, 0), (w, bottom), color)

    def scroll(self, dx, dy) :
        self.voffset = (self.voffset - dy + self.height) % self.height
        self.tft.vscroll(self.voffset)

    def hline(self, x, y, w, color) :
        self.tft.hline((x, self._abs2tft(y)), w, color)

    def text(self, c, x, y, color) :
        self.tft.char((x, self._abs2tft(y)), c, color, self.font, (1, 1))
