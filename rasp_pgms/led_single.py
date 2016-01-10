import Tkinter
from Tkinter import *
import RPi.GPIO as GPIO  ## Import GPIO library

## GPIO_7 -> +(long_leg) LED -ve(short_leg) -> 225 Ohm -> GND(GPIO_6)

GPIO.setwarnings(False) ## To mute warnings at runtime
GPIO.setmode(GPIO.BOARD) ## Use Board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

def ledON():
    GPIO.output(7, True) ## Turn on GPIO pin 7

def ledOFF():
    GPIO.output(7, False) ## Turn off GPIO pin 7

def cleanup():
    GPIO.cleanup()
    exit()

frame = Tkinter.Tk()
# Adding 2 buttons to turn on/off the LED
b1 = Button(frame, text="ON", command=ledON)
b2 = Button(frame, text="OFF", command=ledOFF)
b1.pack()
b2.pack()
frame.mainloop()

