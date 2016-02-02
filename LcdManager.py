import Adafruit_CharLCD as LCD
import time


class LcdManager:

    lcd = None
    message = "Welcome to Corner Pocket\n"
    updateInterval = 1

    def __init__(self):
        print("Initializing LCD Display")
        #self.lcd = LCD.Adafruit_CharLCD()

    def set_message(self, message):
        assert isinstance(message, str)
        self.message = message

    def display_timed_message(self, duration, message):
        message_tmp = self.message
        self.message = message
        time.sleep(duration)
        self.message = message_tmp

    def run_screen(self):
        while True:
            #self.lcd.clear()
            #self.lcd.message(self.message)
            print(self.message)
            time.sleep(self.updateInterval)
