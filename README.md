# Raspberry Pi fan control

This little tool allows to control a 5V fan according to high/low temperature thresholds.

It should be noted that it is possible to run a fan directly by connecting it to a 5V pin (or 3.3V for lower speed/noise) and a ground pin. 
However, in this case this means that the fan will always run.
Here the script **fan.py** turns the fan on and off when temperature exceeds thresholds with the help of a GPIO pin (General Purpose Input/Output).
Powering on/off the fan is done through the help of a switch: a NPN transistor. 

