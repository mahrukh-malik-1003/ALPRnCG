import RPi.GPIO as GPIO
import time
import sys

RED = 22
GREEN = 16
YELLOW = 18

SENSOR = 12


def all_leds_off():
    global RED, GREEN, YELLOW, SENSOR

    for pin in [RED, GREEN, YELLOW]:
        GPIO.output(pin, 0)

def signal_start():
    global RED, GREEN, YELLOW, SENSOR

    print("Starting signal")
    all_leds_off()
    GPIO.output(GREEN, 1)


def signal_stop():
    global RED, GREEN, YELLOW, SENSOR

    print("Stopping signal")
    all_leds_off()
    GPIO.output(YELLOW, 1)
    time.sleep(3)
    GPIO.output(YELLOW, 0)
    GPIO.output(RED, 1)

def setup():
    global RED, GREEN, YELLOW, SENSOR

    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(SENSOR, GPIO.IN)

if '__main__' == __name__:
    
    
    setup()
    signal_stop()

    stopped = True

    while True:
        signal_status = GPIO.input(SENSOR)
        print(signal_status)
        if stopped and not signal_status:
            signal_start()
            stopped = False
        elif not stopped and signal_status:
            signal_stop()
            stopped = True
        
        time.sleep(0.5)
