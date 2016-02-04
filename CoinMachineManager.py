#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import signal
import sys
import locale


class CoinMachineManager:

    # Constants
    PIN_COIN_INTERRUPT = 21
    PULSE_INTERVAL = 0.5
    PULSES_DOLLAR = 10
    PULSES_TOONIE = 20
    MAXIMUM_TIME = 60*60*2
    MINIMUM_TIME = 60*30
    TIMEOUT_INTERVAL = 20

    # Managers
    lcd_manager = None
    light_manager = None

    # Variables
    is_locked = False
    money = 0.00
    lastImpulse = 0
    pulses = 0
    price_per_hour = 5.00

    def __init__(self, lcd_manager, light_manager):
        print("Initializing Coin Manager")
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')
        self.lcd_manager = lcd_manager
        self.light_manager = light_manager

        # Setup coin interrupt channel
        print("Setting Pin: {0} to Input mode, pulled down".format(self.PIN_COIN_INTERRUPT))
        GPIO.setup(self.PIN_COIN_INTERRUPT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.PIN_COIN_INTERRUPT, GPIO.RISING, callback=self.coin_event_handler)

    def coin_event_handler(self, pin):
        print("New Coin Detected")
        self.lastImpulse = time.time()
        self.pulses += 1

    def run_machine(self):
        while True:
            time.sleep(0.5)

            time_since_inpulse = time.time() - self.lastImpulse

            if(self.money>0):
                time_scalar = (self.money/self.price_per_hour)
                time_in_seconds = int(time_scalar*60*60)

                if(time_since_inpulse > self.TIMEOUT_INTERVAL and time_in_seconds > self.MINIMUM_TIME):
                    # Timedout, user is no longer inserting money into the machine
                    self.light_manager.set_active_time(time_in_seconds)
                    self.money = 0.00

            if((time_since_inpulse > self.PULSE_INTERVAL)):

                if(self.pulses > 0 and self.pulses < self.PULSES_DOLLAR):
                    # line interference must be happening, reset the pulses back down to zero
                    self.pulses = 0
                # Check the number of pulses received, if valid add to money counter
                elif(self.pulses >= self.PULSES_DOLLAR and self.pulses < self.PULSES_TOONIE):
                    self.pulses = 0
                    self.money+=1.00
                    self.lcd_manager.set_message(1,"Money: {0}".format(locale.currency(self.money)))
                    # New currency has been added, tell the Lights class
                elif(self.pulses >= self.PULSES_TOONIE):
                    self.pulses = 0
                    self.money+=2.00
                    self.lcd_manager.set_message(1,"Money: {0}".format(locale.currency(self.money)))
                    # New currency has been added, tell the Lights class
