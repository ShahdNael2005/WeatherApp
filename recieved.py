# Imports go at the top
from microbit import *
import radio

weather = " "
temp = " "

mode = 1
nextday = 1

radio.on()
while True:
    message = radio.receive()
    if message:
        weather = message
    if mode == 1:
        display.scroll(weather)
    else:
        display.scroll(temperature())
    if button_a.was_pressed():
        if mode == 1:
            mode = 2
        else:
            mode = 1

        
