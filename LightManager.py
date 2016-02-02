import RPi.GPIO as GPIO
import time
import LcdManager

# This class manages the control of lights via a powerswitch tail
class LightManager:

    PIN_LIGHT = 10

    # remaining time in seconds
    activeTime = 0
    override = False

    # Keeping a reference to LCD Manager so we can update text from here
    lcd_manager = None

    def __init__(self, lcd_manager):
        print("Initializing Light Manager")
        GPIO.setup(self.PIN_LIGHT, GPIO.OUT)
        self.lcd_manager = lcd_manager

    def add_time_to_active(self, seconds):
        """add additional time to active (input in seconds expected)"""
        assert isinstance(seconds, int)
        self.activeTime+=seconds

    def set_override(self, enabled):
        print("Setting Light Manager Override")
        assert isinstance(enabled, bool)
        self.override = enabled
        if(self.override):
            self.lcd_manager.set_message("OVERRIDE ACTIVE")

    def run_lights(self):
        while True:
            time.sleep(0.5)
            # Check the time remaining, if there is no more time and the online override is not currently active
            # disable the light

            if self.override or (time.time() - self.activeTime > 0):
                GPIO.output(self.PIN_LIGHT, True)
            else:
                GPIO.output(self.PIN_LIGHT, False)
