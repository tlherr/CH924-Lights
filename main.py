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

import sys, os, traceback, optparse
import time
import threading
from CoinMachineManager import CoinMachineManager
from LightManager import LightManager
from LcdManager import LcdManager
from HTTPServerManager import HTTPServerManager


def main():

    # Initialize our Classes
    lcd = LcdManager()
    lights = LightManager(lcd)

    lcd_thread = threading.Thread(target=lcd.run_screen,args=())
    lcd_thread.daemon = True
    lcd_thread.start()

    light_thread = threading.Thread(target=lights.run_lights,args=())
    light_thread.daemon = True
    light_thread.start()

    # Just Testing
    lights.set_override(True)

    # Keep the main thread "alive"
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