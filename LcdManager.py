import Adafruit_CharLCD as LCD


class LcdManager:

    lcd = None
    message = ""

    def __init__(self):
        self.lcd = LCD.Adafruit_CharLCD()

    def set_message(self, message):
        assert isinstance(message, str)
        self.message = message

    def display_timed_message(self, time, message):
        message_tmp = self.message
        self.message = message
        time.sleep(time)
        self.message = message_tmp

    def run_screen(self):
        while True:
            self.lcd.clear()
            self.lcd.message(self.message)
