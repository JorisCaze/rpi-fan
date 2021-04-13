#!/usr/bin/env python3

"""test-circuit.py allows to quickly try if the electronic circuit is working and all
dependencies are correctly installed.
"""

from gpiozero import OutputDevice, CPUTemperature
import time

gpio_pin = 4 # Which GPIO pin used to control the fan

if __name__ == '__main__':
    fan = OutputDevice(gpio_pin)

    while True:
        run = int(input("Start[1] / Stop[0]? "))
        if run != 0:
            fan.on()
        else: 
            fan.off()
        time.sleep(2)