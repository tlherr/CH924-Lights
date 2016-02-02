#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import signal
import sys


class CoinMachineManager:

    # Constants
    PIN_COIN_INTERRUPT = 40
    PULSE_INTERVAL = 0.5
    PULSES_DOLLAR = 10
    PULSES_TOONIE = 20

    # Managers
    lcd_manager = None
    light_manager = None

    # Variables
    isLocked = False
    cash = 0.00
    lastImpulse = 0
    pulses = 0
    pricePerHour = 5.00

    def __init__(self, lcd_manager, light_manager):

        self.lcd_manager = lcd_manager
        self.light_manager = light_manager

        ## Setup coin interrupt channel
        print("Setting Pin: {0} to Input mode, pulled down".format(self.PIN_COIN_INTERRUPT))
        GPIO.setup(self.PIN_COIN_INTERRUPT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.PIN_COIN_INTERRUPT, GPIO.RISING, callback=self.coin_event_handler)

        signal.signal(signal.SIGINT, self.signal_handler)        # SIGINT = interrupt by CTRL-C

    def coin_event_handler(self, pin):
        self.lastImpulse = time.time()
        self.pulses = self.pulses + 1

    def run_machine(self):
        while True:
            time.sleep(0.5)
            # Check the current time against the time the last pulse was received
            # If the difference between the two is greater than our interval
            if((time.time() - self.lastImpulse > self.PULSE_INTERVAL) and (self.pulses > 0)):
                # Check the number of pulses received, if valid add to cash counter
                if(self.pulses==self.PULSES_DOLLAR):
                    self.cash+=1.00
                    self.lcd_manager.display_timed_message(20, "{0} Added. Current Total: {1}".format(1.00, self.cash))
                    # New currency has been added, tell the Lights class
                elif(self.pulses==self.PULSES_TOONIE):
                    self.cash+=2.00
                    self.lcd_manager.display_timed_message(20, "{0} Added. Current Total: {1}".format(2.00, self.cash))
                    # New currency has been added, tell the Lights class
                else:
                    # Invalid Coins
                    self.lcd_manager.display_timed_message(20, "Invalid Coin Provided")
                self.pulses = 0



    @staticmethod
    def signal_handler(signal, frame):
        print('You pressed Ctrl+C, exiting')
        GPIO.cleanup()
        sys.exit(0)
