#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import locale


class CoinMachineManager:
    # Constants
    PIN_COIN_INTERRUPT = 21
    PULSE_INTERVAL = 0.5
    PULSES_DOLLAR = 10
    PULSES_TOONIE = 20
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
        GPIO.add_event_detect(self.PIN_COIN_INTERRUPT, GPIO.RISING, callback=self.coin_event_handler, bouncetime=100)

    def set_price_per_hour(self, rate):
        self.price_per_hour = rate
        self.lcd_manager.set_message(1, "Per Hour: {0}".format(locale.currency(self.price_per_hour)))

    def coin_event_handler(self, pin):
        # print("Pulse Detected on Pin: {0}. Current Count: {1}".format(pin, self.pulses))
        self.lastImpulse = time.time()
        self.pulses += 1

    def run_machine(self):
        while True:
            time_since_impulse = time.time() - self.lastImpulse

            # Check for coin pulses to convert into dollar amount that has been entered into coin machine
            if time_since_impulse > self.PULSE_INTERVAL:
                # If the pulses are below our lowest coin (10 pulses) after a delay assume it is interference and reset
                if 0 < self.pulses < self.PULSES_DOLLAR:
                    self.pulses = 0
                # Check the number of pulses received, if valid add to money counter
                elif self.PULSES_DOLLAR <= self.pulses < self.PULSES_TOONIE:
                    self.pulses -= 10
                    self.money += 1.00
                    if not self.light_manager.is_active():
                        self.lcd_manager.set_message(1, "Money: {0}".format(locale.currency(self.money)))
                elif self.pulses >= self.PULSES_TOONIE:
                    self.pulses -= 20
                    self.money += 2.00
                    if not self.light_manager.is_active():
                        self.lcd_manager.set_message(1, "Money: {0}".format(locale.currency(self.money)))

            # If money has been added and the user is done entering money add the time and reset money
            if self.money > 0:
                if time_since_impulse > self.TIMEOUT_INTERVAL:
                    # Timed out, no money has been inserted in the last 20 seconds.
                    # Assume the user is done entering coins

                    time_scalar = (self.money / self.price_per_hour)
                    time_in_seconds = int(time_scalar * 60 * 60)

                    # Need to have at least the minimum amount required in order to activate
                    if self.light_manager.check_min_time(time_in_seconds):
                        # print("Timeout triggered, converting money into time")
                        # print("Setting Active Time {0}".format(time_in_seconds))
                        # Timed out, user is no longer inserting money into the machine
                        self.light_manager.set_active_time(time_in_seconds)
                        self.lcd_manager.set_message(1, "Per Hour: {0}".format(locale.currency(self.price_per_hour)))
                        # Reset money for a new transaction
                        self.money = 0.00
                    else:
                        self.lcd_manager.set_message(1, "{0} Min Cur {1}".format(
                            locale.currency(self.price_per_hour / 2), locale.currency(self.money)))
