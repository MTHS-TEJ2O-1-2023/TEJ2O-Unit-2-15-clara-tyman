"""
Created by: Clara
Created on: Nov 2023
This module is a Micro:bit MicroPython program moves the LED's on the Microbit around the edge of the screen. 
"""

from microbit import *

# variables
set_pixel = None
loopCounter = 0
led_coordinate = 0

# Setup
display.clear()
display.show(Image.SILLY)
sleep(500)

# Press button A
while True:
    if button_a.is_pressed():
        display.clear()
        loopCounter = 0

        while loopCounter < 5:
            led_coordinate = 0
            while led_coordinate <= 3:
                led_coordinate = 0
                while led_coordinate <= 4:
                    sleep(500)
                    display.set_pixel(led_coordinate, loopCounter, 9)
                    led_coordinate += 1

                    led_coordinate = 0
                    loopCounter += 1
                display.clear()
                sleep(500)
