import Adafruit_CharLCD as LCD
from multiprocessing import Process, Pipe
import time

DEBUG = 1

def debug(message):
    if(DEBUG == 1):
        print('DEBUG: ' + message)

class LcdManager():

    def stop(self, stopMessage):
        debug('Stopping Manager')
        self.updateText(stopMessage)
        time.sleep(self.updateInterval)
        self.lcdUpdate.join()

    def start(self):
        debug('Starting Manager')
        self.lcdUpdate.start()
    def updateText(self, text):
        if(text != self.currentText):
            self.currentText = text
            text_file = open(self.fileName, "w")
            text_file.write(text)
            text_file.close()

    def updateCredit(self, value):
        self.updateText('Cash: {0:.2f} EUR'.format(value))

    def lcdUpdater(self):
        lcd = LCD.Adafruit_CharLCDPlate()
        lcd.clear()
        currentValue = ""
        while 1:
            f = open(self.fileName,'r')
            fileValue = f.readline()
            if(fileValue != currentValue):
                debug('LCD: ' + currentValue + ' -> ' + fileValue)
                currentValue = fileValue
                lcd.clear()
                lcd.message('Hourly Rate\n')
                lcd.message(currentValue)
                time.sleep(self.updateInterval)

    def __init__(self, fileName, updateInterval):
        self.fileName = fileName
        self.currentText = ''
        self.updateInterval = updateInterval
        self.lcdUpdate = Process(target=self.lcdUpdater)
        self.start()