#!/usr/bin/python


from LcdManager import LcdManager
import RPi.GPIO as GPIO


PIN_COIN_INTERRUPT = 7


def main():

    GPIO.setmode(GPIO.BCM)

    ## Setup coin interrupt channel
    GPIO.setup(PIN_COIN_INTERRUPT,GPIO.IN)
    GPIO.add_event_detect(PIN_COIN_INTERRUPT,GPIO.FALLING,callback=coinEventHandler)


def coinEventHandler (pin):
    print pin