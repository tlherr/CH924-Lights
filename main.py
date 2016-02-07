#!/usr/bin/env python
"""
SYNOPSIS

    TODO main [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    TODO This describes how to use this script. This docstring
    will be printed by the script if there is an error or
    if the user requests help (-h or --help).

EXAMPLES

    TODO: Show some examples of how to use this script.

EXIT STATUS

    TODO: List exit codes

AUTHOR

    TODO: Thomas Herr <tom@tlherr.com>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.

VERSION

    $0.1$
"""

import sys, os, traceback, optparse, signal
import RPi.GPIO as GPIO
import time
import threading
from CoinMachineManager import CoinMachineManager
from LightManager import LightManager
from LcdManager import LcdManager
from HTTPServerManager import HTTPServerManager


def main():

    # The GPIO.BOARD option specifies that you are referring to the pins by the number of the pin the the plug the numbers printed on the board (e.g. P1)
    # The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number,
    print("Setting GPIO Mode: {0} on board type: {1}".format(GPIO.BCM, GPIO.RPI_REVISION))
    GPIO.setmode(GPIO.BCM)

    # Initialize our Classes, each manager runs its own loop in its own thread
    lcd = LcdManager()
    lights = LightManager(lcd)
    coin_machine = CoinMachineManager(lcd, lights)
    http_server = HTTPServerManager(coin_machine, lights)

    lcd_thread = threading.Thread(target=lcd.run_screen,args=())
    lcd_thread.daemon = True
    lcd_thread.start()

    light_thread = threading.Thread(target=lights.run_lights,args=())
    light_thread.daemon = True
    light_thread.start()

    coin_thread = threading.Thread(target=coin_machine.run_machine,args=())
    coin_thread.daemon = True
    coin_thread.start()

    httpd_thread = threading.Thread(target=http_server.start_server,args=())
    httpd_thread.daemon = True
    httpd_thread.start()

    print("All Threads Running. Application Ready")


    # Keep the main thread "alive", while stuff is done on the others
    while True:
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)