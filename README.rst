Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-pixel-framebuf/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/pixel_framebuf/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_Pixel_Framebuf/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_Pixel_Framebuf/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Neopixel and Dotstar Framebuffer Helper


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit LED Animation <https://github.com/adafruit/Adafruit_CircuitPython_LED_Animation>`_
* `Adafruit framebuf <https://github.com/adafruit/Adafruit_CircuitPython_framebuf>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-pixel_framebuf/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-pixel-framebuf

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-pixel-framebuf

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-pixel-framebuf

Usage Example
=============

.. code-block:: python

    """
    This example runs on an Adafruit NeoPixel Feather
    """
    import board
    import neopixel
    from adafruit_pixel_framebuf import PixelFramebuffer

    pixel_pin = board.D6
    pixel_width = 8
    pixel_height = 4

    pixels = neopixel.NeoPixel(
        pixel_pin,
        pixel_width * pixel_height,
        brightness=0.1,
        auto_write=False,
    )

    pixel_framebuf = PixelFramebuffer(
        pixels,
        pixel_width,
        pixel_height,
        alternating=False,
    )

    pixel_framebuf.fill(0x000088)
    pixel_framebuf.pixel(5, 1, 0xFFFF00)
    pixel_framebuf.line(0, 0, pixel_width - 1, pixel_height - 1, 0x00FF00)
    pixel_framebuf.display()

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/pixel_framebuf/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_Pixel_Framebuf/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
