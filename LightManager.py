import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
import LcdManager

# This class manages the control of lights via a powerswitch tail
class LightManager:

    PIN_LIGHT = 20

    activation_time = None
    expiration_time = None
    # remaining time in seconds
    override = False

    # Keeping a reference to LCD Manager so we can update text from here
    lcd_manager = None

    def __init__(self, lcd_manager):
        print("Initializing Light Manager")
        GPIO.setup(self.PIN_LIGHT, GPIO.OUT)
        self.lcd_manager = lcd_manager

    def set_active_time(self, seconds):
        assert isinstance(seconds, int)
        self.activation_time = time.time()
        self.expiration_time = self.activation_time + timedelta(seconds=seconds)

    def add_time_to_active(self, seconds):
        """add additional time to active (input in seconds expected)
        :type seconds: int
        """
        assert isinstance(seconds, int)
        self.activeTime += seconds
        self.expiration_time = self.expiration_time + timedelta(seconds=seconds)

    @staticmethod
    def seconds_to_time(seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return "%d:%02d:%02d" % (h, m, s)

    def set_override(self, enabled):
        print("Setting Light Manager Override")
        assert isinstance(enabled, bool)
        self.override = enabled
        if(self.override):
            self.lcd_manager.set_message(0, "OVERRIDE ACTIVE")
            self.lcd_manager.lcd.set_color(1.0, 0.0, 0.0)

    def run_lights(self):
        while True:
            time.sleep(0.5)
            # Check the time remaining, if there is no more time and the online override is not currently active
            # disable the light

            if self.override:
                GPIO.output(self.PIN_LIGHT, True)
            elif self.expiration_time - time.time() > 0:
                GPIO.output(self.PIN_LIGHT, True)
                self.lcd_manager.set_message(0, "{0} Left".format(self.seconds_to_time(self.expiration_time - time.time())))
            else:
                GPIO.output(self.PIN_LIGHT, False)
                self.lcd_manager.lcd.set_color(0.0, 0.0, 1.0)
