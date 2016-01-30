#!/usr/bin/python


from LcdManager import LcdManager
import RPi.GPIO as GPIO
import time
import signal
import sys


PIN_COIN_INTERRUPT = 7


def main():

    GPIO.setmode(GPIO.BCM)

    ## Setup coin interrupt channel
    GPIO.setup(PIN_COIN_INTERRUPT,GPIO.IN)
    GPIO.add_event_detect(PIN_COIN_INTERRUPT,GPIO.FALLING,callback=coinEventHandler)

    signal.signal(signal.SIGINT, signal_handler)	# SIGINT = interrupt by CTRL-C

    while True:
        time.sleep(0.5)


def signal_handler(signal, frame):
    print('You pressed Ctrl+C, so exiting')
    GPIO.cleanup()
    sys.exit(0)


def coinEventHandler (pin):
    print pin




if __name__=="__main__":
    main()