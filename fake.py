# Replace libraries by fake ones
import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi    # Fake RPi (GPIO)


import app