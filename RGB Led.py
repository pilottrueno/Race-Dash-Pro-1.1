Светодиодная лента.

from rpi_ws281x import PixelStrip, Color

LED_COUNT = 8
LED_PIN = 18

strip = PixelStrip(LED_COUNT, LED_PIN)
strip.begin()