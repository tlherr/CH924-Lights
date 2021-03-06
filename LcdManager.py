import Adafruit_CharLCD as LCD
import time


class LcdManager:

    # Variables
    lcd = None
    message_top = ">Corner  Pocket<"
    message_bottom = "Per Hour: $5.00"
    updateInterval = 1

    def __init__(self):
        print("Initializing LCD Display")
        self.lcd = LCD.Adafruit_CharLCDPlate()
        self.lcd.set_color(0.0, 0.0, 1.0)

    def set_message(self, line, message):
        assert isinstance(line, int)
        assert isinstance(message, str)
        if line == 0:
            self.message_top = message
        elif line == 1:
            self.message_bottom = message

    def get_message(self):
        return "{0}\n{1}".format(self.message_top, self.message_bottom)

    def display_timed_message(self, duration, message):
        message_top_tmp = self.message_top
        message_bottom_tmp = self.message_bottom
        self.message_top = message
        self.message_bottom = ""
        time.sleep(duration)
        self.set_message(0, message_top_tmp)
        self.set_message(1, message_bottom_tmp)

    def run_screen(self):
        while True:
            self.lcd.clear()
            self.lcd.message(self.get_message())
            time.sleep(self.updateInterval)
