import RPi.GPIO as GPIO
import time
import Tkinter
from Tkinter import *

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


def stop():
    GPIO.output(11, False) ## Turn off GPIO pin 7
    GPIO.output(7, False) ## Turn off GPIO pin 7
    GPIO.output(13, False) ## Turn on GPIO pin 7
    GPIO.output(15, False) ## Turn on GPIO pin 7

def left():
    GPIO.output(7, False) ## Turn off GPIO pin 7
    GPIO.output(11, True) ## Turn off GPIO pin 7
    GPIO.output(13, False) ## Turn on GPIO pin 7
    GPIO.output(15, False) ## Turn on GPIO pin 7

def right():
    GPIO.output(7, False) ## Turn off GPIO pin 7
    GPIO.output(11, False) ## Turn off GPIO pin 7
    GPIO.output(13, False) ## Turn on GPIO pin 7
    GPIO.output(15, True) ## Turn on GPIO pin 7

def front():
    GPIO.output(7, False) ## Turn off GPIO pin 7
    GPIO.output(11, True) ## Turn off GPIO pin 7
    GPIO.output(13, False) ## Turn on GPIO pin 7
    GPIO.output(15, True) ## Turn on GPIO pin 7

def back():
    GPIO.output(11, False) ## Turn off GPIO pin 7
    GPIO.output(7, True) ## Turn off GPIO pin 7
    GPIO.output(15, False) ## Turn on GPIO pin 7
    GPIO.output(13, True) ## Turn on GPIO pin 7

def setup():
	frame = Tkinter.Tk()
	# Adding 2 buttons to turn on/off the LED
	b1 = Button(frame, text="LEFT", command=left)
	b2 = Button(frame, text="RIGHT", command=right)
	b3 = Button(frame, text="FRONT", command=front)
	b4 = Button(frame, text="BACK", command=back)
	b5 = Button(frame, text="STOP!!!", command=stop)
	b1.pack()
	b2.pack()
	b3.pack()
	b4.pack()
	b5.pack()
	frame.mainloop()

def destroy():
	GPIO.output(7, False) # motor stop
	GPIO.cleanup()        # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

#GPIO.output(7, True)
#time.sleep(5)

#GPIO.output(7, False)
#GPIO.output(11, True)
#time.sleep(5)

#GPIO.output(11, False)
#GPIO.output(7, True)
#time.sleep(5)
#
#GPIO.output(7, False)
#GPIO.output(11, True)
#time.sleep(5)
#
#GPIO.output(11, False)
#GPIO.output(7, True)
#time.sleep(5)
#
#GPIO.cleanup()
####
