#!/usr/bin/python


from LcdManager import LcdManager
import RPi.GPIO as GPIO
import time
import signal
import sys
from decimal import Decimal
import threading
from HTTPServer import HTTPServer



# Constants
PIN_COIN_INTERRUPT = 40
PULSE_INTERVAL = 0.5


# Variables
cash = 0.00
lastImpulse = 0
pulses = 0

def main():

    global pulses
    global cash
    global lastImpulse

    # The GPIO.BOARD option specifies that you are referring to the pins by the number of the pin the the plug the numbers printed on the board (e.g. P1)
    # The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number,
    print("Setting GPIO Mode to Board")
    GPIO.setmode(GPIO.BOARD)

    ## Setup coin interrupt channel
    print("Setting Pin: {0} to Input mode, pulled down".format(PIN_COIN_INTERRUPT))
    GPIO.setup(PIN_COIN_INTERRUPT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(PIN_COIN_INTERRUPT, GPIO.RISING, callback=coinEventHandler)

    server = HTTPServer()

    print("Starting server on new thread")
    serverThread = threading.Thread(target=server.start_server,
        args=(),
        kwargs={},
    )
    serverThread.daemon = True
    serverThread.start()


    signal.signal(signal.SIGINT, signal_handler)	# SIGINT = interrupt by CTRL-C

    while True:
        time.sleep(0.5)
        # Check the current time against the time the last pulse was received
        # If the difference between the two is greater than our interval
        if((time.time() - lastImpulse > PULSE_INTERVAL) and (pulses > 0)):
            if(pulses==10):
                cash+=1.00
            elif(pulses==20):
                cash+=2.00
            else:
                # Invalid Coins
                print("Invalid Coin Received")

            print "Pulses: {0}".format(pulses)
            print "Cash: {0}".format(cash)
            pulses = 0

def signal_handler(signal, frame):
    print('You pressed Ctrl+C, exiting')
    GPIO.cleanup()
    sys.exit(0)


def coinEventHandler(pin):
    global lastImpulse
    global pulses
    lastImpulse = time.time()
    pulses = pulses + 1
    print "Pulse"



if __name__=="__main__":
    main()