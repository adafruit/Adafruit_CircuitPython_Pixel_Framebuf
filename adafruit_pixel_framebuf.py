# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_pixel_framebuf`
================================================================================

Neopixel and Dotstar Framebuffer Helper


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* `Adafruit NeoPixels <https://www.adafruit.com/category/168>`_
* `Adafruit DotStars <https://www.adafruit.com/category/885>`_
* `Flexible 8x32 NeoPixel RGB LED Matrix <https://www.adafruit.com/product/2294>`_
* `Flexible 16x16 NeoPixel RGB LED Matrix <https://www.adafruit.com/product/2547>`_
* `Flexible 8x8 NeoPixel RGB LED Matrix <https://www.adafruit.com/product/2612>`_
* `Adafruit NeoPixel 8x8 NeoMatrices <https://www.adafruit.com/product/3052>`_
* `Adafruit DotStar High Density 8x8 Grid <https://www.adafruit.com/product/3444>`_
* `Adafruit NeoPixel FeatherWing <https://www.adafruit.com/product/2945>`_
* `Adafruit DotStar FeatherWing <https://www.adafruit.com/product/3449>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

* Adafruit's LED Animation library:
  https://github.com/adafruit/Adafruit_CircuitPython_LED_Animation
* Adafruit's framebuf library: https://github.com/adafruit/Adafruit_CircuitPython_framebuf

"""

# imports

from micropython import const
import adafruit_framebuf
from adafruit_led_animation.grid import PixelGrid

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Pixel_Framebuf.git"

HORIZONTAL = const(1)
VERTICAL = const(2)


class PixelFramebuffer:
    """
    NeoPixel and Dotstar FrameBuffer for easy drawing and text on a
    grid of either kind of pixel
    """

    def __init__(
        self,
        pixels,
        width,
        height,
        orientation=HORIZONTAL,
        alternating=True,
        reverse_x=False,
        reverse_y=False,
        top=0,
        bottom=0,
        rotation=0,
    ):  # pylint: disable=too-many-arguments
        self._width = width
        self._height = height

        self._grid = PixelGrid(
            pixels,
            width,
            height,
            orientation,
            alternating,
            reverse_x,
            reverse_y,
            top,
            bottom,
        )

        self._buffer = bytearray(width * height * 3)
        self._framebuf = adafruit_framebuf.FrameBuffer(
            self._buffer, width, height, buf_format=adafruit_framebuf.RGB888
        )
        self.rotation = rotation

    def pixel(self, x, y, color=None):
        """draw a single pixel in the display buffer"""
        self._framebuf.pixel(x, y, color)

    def fill(self, color):
        """fill the screen with the passed color"""
        self._framebuf.fill(color)

    def rect(self, x, y, width, height, color):  # pylint: disable=too-many-arguments

        """draw a rectangle"""
        self._framebuf.rect(x, y, width, height, color)

    def fill_rect(
        self, x, y, width, height, color
    ):  # pylint: disable=too-many-arguments
        """fill a rectangle with the passed color"""
        self._framebuf.fill_rect(x, y, width, height, color)

    def line(self, x_0, y_0, x_1, y_1, color):  # pylint: disable=too-many-arguments
        """Draw a line from (x_0, y_0) to (x_1, y_1) in passed color"""
        self._framebuf.line(x_0, y_0, x_1, y_1, color)

    def text(self, string, x, y, color, *, font_name="font5x8.bin"):
        """Write text string at location (x, y) in given color, using font file"""
        self._framebuf.text(string, x, y, color, font_name=font_name)

    def hline(self, x, y, width, color):
        """draw a horizontal line"""
        self._framebuf.hline(self, x, y, width, color)

    def vline(self, x, y, height, color):
        """draw a vertical line"""
        self._framebuf.vline(self, x, y, height, color)

    def circle(self, center_x, center_y, radius, color):
        """Draw a circle at the given midpoint location, radius and color.
        The ```circle``` method draws only a 1 pixel outline."""
        self._framebuf.circle(center_x, center_y, radius, color)

    def image(self, image):
        """Set buffer to value of Python Imaging Library image.  The image should
        be in RGB mode and a size equal to the display size.
        """
        self._framebuf.image(image)

    def display(self):
        """Copy the raw buffer to the grid and show"""
        for _y in range(self._height):
            for _x in range(self._width):
                index = (_y * self._framebuf.stride + _x) * 3
                self._grid[(_x, _y)] = tuple(self._buffer[index : index + 3])
        self._grid.show()

    @property
    def width(self):
        """The width of the display, accounting for rotation"""
        if self.rotation in (0, 2):
            return self._width
        return self._height

    @property
    def height(self):
        """The height of the display, accounting for rotation"""
        if self.rotation in (0, 2):
            return self._height
        return self._width

    @property
    def rotation(self):
        """The rotation of the display, can be one of (0, 1, 2, 3)"""
        return self._framebuf.rotation

    @rotation.setter
    def rotation(self, val):
        self._framebuf.rotation = val
