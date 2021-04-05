# Write your code here :-)
import sys, time
import RPi.GPIO as GPIO

redPin   = 11
greenPin = 13
bluePin  = 15

button = 37

option = 1

def button_callback(channel):
    global option
    if option == 1:
        redOn()
    elif option == 2:
        redOff()
    elif option == 3:
        blueOn()
    elif option == 4:
        blueOff()
    elif option == 5:
        greenOn()
    elif option == 6:
        greenOff()
    elif option == 7:
        blueishOn()
    elif option == 8:
        blueishOff()
    elif option == 9:
        yellowOn()
    elif option == 10:
        yellowOff()
    elif option == 11:
        purpleOn()
    else:
        purpleOff()
    #refactor here, spaghetti code ^
    if option <= 12:
        option +=1
    else:
        option = 1



def set_pushdown():
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(button,GPIO.RISING,callback=button_callback)

def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

def redOn():
	blink(redPin)

def greenOn():
	blink(greenPin)

def blueOn():
	blink(bluePin)

def yellowOn():
    blink(redPin)
    blink(greenPin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)
    
def blueishOn():
    blink(greenPin)
    blink(bluePin)
    
def blueishOff():
    turnOff(greenPin)
    turnOff(bluePin)
    
def purpleOn():
    blink(redPin)
    blink(bluePin)
    
def purpleOff():
    turnOff(redPin)
    turnOff(bluePin)
    
def redOff():
	turnOff(redPin)

def greenOff():
	turnOff(greenPin)

def blueOff():
	turnOff(bluePin)

def main():
    set_pushdown()
    message = input("Press enter to quit\n\n")
    GPIO.cleanup() # Clean up

main()