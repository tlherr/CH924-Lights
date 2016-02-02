import Adafruit_CharLCD as LCD
import time


class LcdManager:
    lcd = None
    message = "Welcome to Corner Pocket\n"
    updateInterval = 1

    lcd_rs = 27  # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en = 22
    lcd_d4 = 25
    lcd_d5 = 24
    lcd_d6 = 23
    lcd_d7 = 18
    lcd_backlight = 4

    lcd_columns = 16
    lcd_rows = 2

    def __init__(self):
        print("Initializing LCD Display")
        self.lcd = LCD.Adafruit_CharLCD(self.lcd_rs, self.lcd_en, self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7,
                                        self.lcd_columns, self.lcd_rows, self.lcd_backlight)

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
            self.lcd.clear()
            self.lcd.message(self.message)
            # print(self.message)
            time.sleep(self.updateInterval)
