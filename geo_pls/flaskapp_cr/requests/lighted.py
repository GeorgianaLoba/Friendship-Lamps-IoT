# Write your code here :-)
import sys, time, requests, threading, urllib3
import RPi.GPIO as GPIO

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://flaskapp-cr-v1-usiuscltvq-ew.a.run.app"

global tired

redPin = 11
greenPin = 13
bluePin = 15

button = 37
shutdown = 40

def turnAllOff():
    redOff()
    blueOff()
    greenOff()

def button_callback(channel):
    # get what was before then increment it to switch to another colour
    resp = requests.get(f"{url}/getopt", verify=False)
    # the response from the server looks like this {"option":2} hence the way the split below is performed
    option = int(resp.content.decode().split(":")[1].split("}")[0])
    if option < 6:
        option += 1
    else:
        option = 1
    # send new colour
    requests.get(f"{url}/setopt/{option}", verify=False)
    # light the colour
    lightAccording(option)

def shutit(args):
    # switches the led to block or accept lighting of led
    turnAllOff()
    global tired
    if tired == 0:
        tired = 1
        print("I'm going off, you are annoying!")
    else:
        tired = 0
        print("Hey friend, I'm back!")


def set_pushdown():
    GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # bouncetime refer to button sensitivity
    GPIO.add_event_detect(button, GPIO.RISING, callback=button_callback, bouncetime=200)


def set_shutdown():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(shutdown, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(shutdown, GPIO.RISING, callback=shutit, bouncetime=200)


def blink(pin):
    # light a light pin (the RGB led has 3 for example)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)


def turnOff(pin):
    # turn off the light on specified pin
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


def lightAccording(option):
    # will light the relevant pins for the option is the lamp is 'on'
    global tired
    if tired == 0:
        turnAllOff()
        if option == 1:
            redOn()
        elif option == 2:
            blueOn()
        elif option == 3:
            greenOn()
        elif option == 4:
            blueishOn()
        elif option == 5:
            yellowOn()
        else:
            purpleOn()
    else:
        print("I'm turned off, stop!!! ohmygod")

def synced():
    # after a set amount of time, perform a request call to the server site to put the lamps in sync
    threading.Timer(5, synced).start()
    resp = requests.get(f"{url}/getopt", verify=False)
    # the response from the server looks like this {"option":2} hence the way the split below is performed
    option = int(resp.content.decode().split(":")[1].split("}")[0])
    # sync the lamp with the correct option
    lightAccording(option)


def main():
    global tired
    # 1 means lamp is off, 0 means it's on
    tired = 0
    # just to be sure, turn off all LEDs
    turnAllOff()
    # init the buttons with their callbacks
    set_pushdown()
    set_shutdown()
    # for syncing all clients/lamps connected to the server
    synced()
    message = input("Press enter to quit\n\n")
    # Clean up
    GPIO.cleanup()


main()
