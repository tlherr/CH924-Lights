import RPi.GPIO as GPIO
import time
import LcdManager


# This class manages the control of lights via a powerswitch tail
class LightManager:
    PIN_LIGHT = 20
    MAXIMUM_TIME = 60 * 60 * 2
    MINIMUM_TIME = 60 * 30

    activation_time = None
    time_remaining = None
    expiration_time = None
    # remaining time in seconds
    override = False

    # Keeping a reference to LCD Manager so we can update text from here
    lcd_manager = None

    def __init__(self, lcd_manager):
        print("Initializing Light Manager")
        GPIO.setup(self.PIN_LIGHT, GPIO.OUT)
        self.lcd_manager = lcd_manager

    def check_time(self, seconds):
        assert isinstance(seconds, int)
        if seconds < self.MINIMUM_TIME:
            return False
        elif seconds > self.MAXIMUM_TIME:
            return False
        else:
            return True

    def set_active_time(self, seconds):
        assert isinstance(seconds, int)

        self.activation_time = time.time()
        if seconds > self.MAXIMUM_TIME:
            self.expiration_time = self.MAXIMUM_TIME
        else:
            self.expiration_time = self.activation_time + seconds

        self.time_remaining = self.expiration_time - time.time()
        self.lcd_manager.lcd.set_color(0.0, 1.0, 0.0)

    def add_time_to_active(self, seconds):
        """add additional time to active (input in seconds expected)
        :type seconds: int
        """
        assert isinstance(seconds, int)
        self.time_remaining += seconds
        self.expiration_time += seconds

    @staticmethod
    def seconds_to_time(seconds):
        """Formatting method for general use, converts time in seconds to human readable format
        :type seconds: int
        """
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return "%d:%02d:%02d" % (h, m, s)

    def set_override(self, enabled):
        print("Setting Light Manager Override")
        assert isinstance(enabled, bool)
        self.override = enabled
        if self.override:
            self.lcd_manager.set_message(0, "OVERRIDE ACTIVE")
            self.lcd_manager.lcd.set_color(1.0, 0.0, 0.0)
        else:
            self.lcd_manager.set_message(0, ">Corner Pocket<")
            self.lcd_manager.lcd.set_color(0.0, 0.0, 1.0)

    def run_lights(self):
        while True:
            time.sleep(1)
            # Check the time remaining, if there is no more time and the online override is not currently active
            # disable the light

            if self.override:
                print("Light Manager Override Detected, Light On")
                GPIO.output(self.PIN_LIGHT, True)
            elif self.time_remaining is not None:
                if self.time_remaining > 0:
                    print("Light Manager Active Time Detected")
                    GPIO.output(self.PIN_LIGHT, True)
                    self.time_remaining = self.expiration_time - time.time()
                    self.lcd_manager.set_message(0, "{0} Left".format(self.seconds_to_time(self.time_remaining)))
                else:
                    print("Light: Disabled")
                    self.lcd_manager.set_message(0, ">Corner Pocket<")
                    self.time_remaining = None
                    GPIO.output(self.PIN_LIGHT, False)
                    self.lcd_manager.lcd.set_color(0.0, 0.0, 1.0)
            else:
                print("Light: Disabled")
                GPIO.output(self.PIN_LIGHT, False)
                self.lcd_manager.lcd.set_color(0.0, 0.0, 1.0)
