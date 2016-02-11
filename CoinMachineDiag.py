#!/usr/bin/python

import sys, os, traceback, optparse, signal
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

    print("Initializing Coin Machine Diagnostic Tool")

    GPIO.setmode(GPIO.BCM)
    # Setup coin interrupt channel
    print("Setting Pin: {0} to Input mode, pulled down".format(PIN_COIN_INTERRUPT))
    GPIO.setup(PIN_COIN_INTERRUPT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(PIN_COIN_INTERRUPT, GPIO.RISING, callback=self.coin_event_handler)

    print("Setting Pin: {0} to Input mode, pulled down".format(PIN_COIN_COUNT))
    GPIO.setup(PIN_COIN_COUNT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(PIN_COIN_COUNT, GPIO.RISING, callback=self.coin_count_handler)

    def coin_event_handler(self, pin):
        print("Pulse Detected on Pin: {0}. Current Count: {1}".format(pin, self.pulses))
        self.lastImpulse = time.time()
        self.pulses += 1

    def coin_count_handler(self, pin):
        print("Pulse Detected on Pin: {0}. Current Count: {1}".format(pin, self.count))
        self.count += 1

    while True:
        time.sleep(1)

if __name__ == '__main__':
    try:
        CoinMachineDiag()
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)