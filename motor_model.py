#!/usr/bin/python

from constants import *
from utils import getCounterValues
from Adafruit_GPIO.GPIO import BaseGPIO as BaseGPIO

class Motor:
    def __init__(self, channel, freq, debug=False):
        self.freq = freq
        self.current_state = 0
        self.channel = channel
        self.debug = debug

    def reset(self, pwm):
        # reset PCA9685
        if self.debug:
            print("Reseting PCA9685")
        on_count, off_count = getCounterValues(delay=0, dc=30)
        on_hex, off_hex = int(hex(on_count), base=16), int(hex(off_count), base=16)
        pwm.setPWMCounters(self.channel, I2C_BUS, on_hex, off_hex)

        # reset TB9051FTG
        # default FWD ENB=1

    def setPWM(self, pwm, dutycycle, delay=0):
        print("Delay: {}, Duty Cycle: {}".format(delay, dutycycle))
        on_count, off_count = getCounterValues(delay, dutycycle)
        on_hex, off_hex = int(hex(on_count), base=16), int(hex(off_count), base=16)

        print("ON: {}, {}, OFF: {}, {}".format(on_count, hex(on_count), off_count, hex(off_count)))
        pwm.setPWMCounters(self.channel, I2C_BUS, on_hex, off_hex)

    def forward(self):

