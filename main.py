#!/usr/bin/python


from LcdManager import LcdManager
import RPi.GPIO as GPIO
import time
import signal
import sys
import decimal

# Constants
PIN_COIN_INTERRUPT = 26

# Variables
cash = 0.00
lastImpulse = 0
pulses = 0


def main():

    # The GPIO.BOARD option specifies that you are referring to the pins by the number of the pin the the plug the numbers printed on the board (e.g. P1)
    # The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number,

    GPIO.setmode(GPIO.BCM)

    ## Setup coin interrupt channel
    GPIO.setup(PIN_COIN_INTERRUPT, GPIO.IN)
    GPIO.add_event_detect(PIN_COIN_INTERRUPT, GPIO.RISING, callback=coinEventHandler)
    #GPIO.add_event_detect(PIN_COIN_INTERRUPT, GPIO.FALLING, callback=coinEventHandler)

    signal.signal(signal.SIGINT, signal_handler)	# SIGINT = interrupt by CTRL-C

    while True:
        time.sleep(0.5)
        if((time.time() - lastImpulse > 0.5) and (pulses > 0)):
            cash = decimal(cash) + decimal(pulses)/decimal(10)
            pulses = 0
            print cash

def signal_handler(signal, frame):
    print('You pressed Ctrl+C, exiting')
    GPIO.cleanup()
    sys.exit(0)


def coinEventHandler (pin):
    global cash
    global lastImpulse
    global pulses
    lastImpulse = time.time()
    pulses = pulses + 1
    print "Pulse"




if __name__=="__main__":
    main()