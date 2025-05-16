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
try:
    from circuitpython_typing.led import FillBasedColorUnion
except ImportError:
    pass

import adafruit_framebuf
from adafruit_led_animation.grid import PixelGrid
from micropython import const

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Pixel_Framebuf.git"

HORIZONTAL: int = const(1)
VERTICAL: int = const(2)


class PixelFramebuffer(adafruit_framebuf.FrameBuffer):
    """
    NeoPixel and Dotstar FrameBuffer for easy drawing and text on a
    grid of either kind of pixel

    :param strip: An object that implements the Neopixel or Dotstar protocol.
    :param width: Framebuffer width.
    :param height: Framebuffer height.
    :param orientation: Orientation of the strip pixels - HORIZONTAL (default) or VERTICAL.
      HORIZONTAL and VERTICAL are primitive integers created by micropython.const(x).
    :param alternating: Whether the strip alternates direction from row to row (default True).
    :param reverse_x: Whether the strip X origin is on the right side (default False).
    :param reverse_y: Whether the strip Y origin is on the bottom (default False).
    :param tuple top: (x, y) coordinates of grid top left corner (Optional)
    :param tuple bottom: (x, y) coordinates of grid bottom right corner (Optional)
    :param int rotation: A value of 0-3 representing the rotation of the framebuffer (default 0)

    """

    def __init__(
        self,
        pixels: FillBasedColorUnion,
        width: int,
        height: int,
        orientation: int = HORIZONTAL,
        alternating: bool = True,
        reverse_x: bool = False,
        reverse_y: bool = False,
        top: int = 0,
        bottom: int = 0,
        rotation: int = 0,
    ) -> None:
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
        self._double_buffer = bytearray(width * height * 3)
        super().__init__(self._buffer, width, height, buf_format=adafruit_framebuf.RGB888)
        self.rotation = rotation

    def blit(self) -> None:
        """blit is not yet implemented"""
        raise NotImplementedError()

    def display(self) -> None:
        """Copy the raw buffer changes to the grid and show"""
        for _y in range(self._height):
            for _x in range(self._width):
                index = (_y * self.stride + _x) * 3
                if self._buffer[index : index + 3] != self._double_buffer[index : index + 3]:
                    self._grid[(_x, _y)] = tuple(self._buffer[index : index + 3])
                    self._double_buffer[index : index + 3] = self._buffer[index : index + 3]
        self._grid.show()
