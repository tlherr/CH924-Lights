#!/usr/bin/python

import RPi.GPIO as GPIO
import time


class CoinMachineDiag:
    # Constants
    PIN_COIN_INTERRUPT = 21
    PIN_COIN_COUNT = 16

    # Variables
    lastImpulse = None
    pulses = 0
    count = 0

    def __init__(self):
        print("Initializing Coin Machine Diagnostic Tool")

        # Setup coin interrupt channel
        print("Setting Pin: {0} to Input mode, pulled down".format(self.PIN_COIN_INTERRUPT))
        GPIO.setup(self.PIN_COIN_INTERRUPT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.PIN_COIN_INTERRUPT, GPIO.RISING, callback=self.coin_event_handler)

        print("Setting Pin: {0} to Input mode, pulled down".format(self.PIN_COIN_COUNT))
        GPIO.setup(self.PIN_COIN_COUNT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.PIN_COIN_COUNT, GPIO.RISING, callback=self.coin_count_handler)

    def coin_event_handler(self, pin):
        print("Pulse Detected on Pin: {0}. Current Count: {1}".format(pin, self.pulses))
        self.lastImpulse = time.time()
        self.pulses += 1

    def coin_count_handler(self, pin):
        print("Pulse Detected on Pin: {0}. Current Count: {1}".format(pin, self.count))
        self.count += 1

    while True:
        time.sleep(1)