#!/usr/bin/env python3

"""fan.py turns a fan on and off when temperature exceeds temperature thresholds.

This script is heavily inspired from
https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c#
https://howchoo.com/g/ote2mjkzzta/control-raspberry-pi-fan-temperature-python#execute-the-fan-controller-code-on-boot-optional
https://raspberrypi.stackexchange.com/questions/62220/how-do-i-control-gpio-connected-fan-via-code-at-a-certain-cpu-temperature

It should be noted that it is possible to run a fan directly by connecting it to GPIO pins
(General Purpose Input Output). The fan can be plugged into 5V GPIO pin (or 3.3V for lower
speed/noise) and ground GPIO pin but this means that the fan will always run.
"""

from gpiozero import OutputDevice, CPUTemperature
import time

high_threshold = 50 # (degrees Celsius) Turn on fan temp.
low_threshold = 45 # (degrees Celsius) Turn off fan temp.
sleep_time = 15 # (seconds) How often we check the core temp.
gpio_pin = 4 # Which GPIO pin used to control the fan

if __name__ == '__main__':
    fan = OutputDevice(gpio_pin)
    cpu = CPUTemperature()

    while True:
        if cpu.temperature > high_threshold and not fan.value:
            fan.on()
        elif fan.value and cpu.temperature < low_threshold:
            fan.off()

        time.sleep(sleep_time)
