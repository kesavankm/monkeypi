import RPi.GPIO as GPIO
import time
import Tkinter
from Tkinter import *

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

M_LEFT_1 = 7 # Motor 
M_LEFT_1 = 11 # Motor 
M_RIGHT_1 = 13
M_RIGHT_2 = 15

GPIO.setup(M_LEFT_1, GPIO.OUT)
GPIO.setup(M_LEFT_2, GPIO.OUT)
GPIO.setup(M_RIGHT_1, GPIO.OUT)
GPIO.setup(M_RIGHT_2, GPIO.OUT)

def stop():
	# Turn off all GPIO pins (stop all motors)
    GPIO.output(M_LEFT_1, False)
    GPIO.output(M_LEFT_2, False)
    GPIO.output(M_RIGHT_1, False)
    GPIO.output(M_RIGHT_2, False)

def forward():
	# Turn both motors in same direction
    GPIO.output(M_LEFT_1, True)
    GPIO.output(M_LEFT_2, False)
    GPIO.output(M_RIGHT_1, True)
    GPIO.output(M_RIGHT_2, False)

def reverse():
	# Turn both motors in opp direction
    GPIO.output(M_LEFT_1, False)
    GPIO.output(M_LEFT_2, True)
    GPIO.output(M_RIGHT_1, False)
    GPIO.output(M_RIGHT_2, True)

def left():
	# Turn ON Right motor 
    GPIO.output(M_LEFT_1, False)
    GPIO.output(M_LEFT_2, False)
    GPIO.output(M_RIGHT_1, True)
    GPIO.output(M_RIGHT_2, False)

def right():
	# Turn OFF Right motor 
    GPIO.output(M_LEFT_1, True)
    GPIO.output(M_LEFT_2, False)
    GPIO.output(M_RIGHT_1, False)
    GPIO.output(M_RIGHT_2, False)

def key_press(event):
    if event.keysym == 'Left':
		left()
    elif event.keysym == 'Right':
        right()
    elif event.keysym == 'Up':
        forward()
    elif event.keysym == 'Down':
		reverse()
    elif event.keysym == 'Space':
		stop()

def key_release(event):
    if event.keysym == 'Space':
		stop()
	

def setup():
    # Adding 2 buttons to start stop
    frame.bind("<KeyPress>", key_press)
    frame.bind("<KeyRelease>", key_release)
    frame.mainloop()

#def stop():
#    GPIO.output(11, False) ## Turn off GPIO pin 7
#    GPIO.output(7, False) ## Turn off GPIO pin 7
#    GPIO.output(13, False) ## Turn on GPIO pin 7
#    GPIO.output(15, False) ## Turn on GPIO pin 7
#
#def left():
#    GPIO.output(7, False) ## Turn off GPIO pin 7
#    GPIO.output(11, True) ## Turn off GPIO pin 7
#    GPIO.output(13, False) ## Turn on GPIO pin 7
#    GPIO.output(15, False) ## Turn on GPIO pin 7
#
#def right():
#    GPIO.output(7, False) ## Turn off GPIO pin 7
#    GPIO.output(11, False) ## Turn off GPIO pin 7
#    GPIO.output(13, False) ## Turn on GPIO pin 7
#    GPIO.output(15, True) ## Turn on GPIO pin 7
#
#def front():
#    GPIO.output(7, False) ## Turn off GPIO pin 7
#    GPIO.output(11, True) ## Turn off GPIO pin 7
#    GPIO.output(13, False) ## Turn on GPIO pin 7
#    GPIO.output(15, True) ## Turn on GPIO pin 7
#
#def back():
#    GPIO.output(11, False) ## Turn off GPIO pin 7
#    GPIO.output(7, True) ## Turn off GPIO pin 7
#    GPIO.output(15, False) ## Turn on GPIO pin 7
#    GPIO.output(13, True) ## Turn on GPIO pin 7

#def setup():
#    frame = Tkinter.Tk()
#    b1 = Button(frame, text="LEFT", command=left)
#    b2 = Button(frame, text="RIGHT", command=right)
#    b3 = Button(frame, text="FRONT", command=front)
#    b4 = Button(frame, text="BACK", command=back)
#    b5 = Button(frame, text="STOP!!!", command=stop)
#    b1.pack()
#    b2.pack()
#    b3.pack()
#    b4.pack()
#    b5.pack()
#    frame.mainloop()

def destroy():
    GPIO.output(7, False) # motor stop
    GPIO.cleanup()        # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
     destroy()

