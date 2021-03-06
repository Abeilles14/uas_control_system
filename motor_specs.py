# motor specs as a dict
MOTORS = {
    # unused
    "pololu_0": {
        "position": "winch",
        "frequency": 300, # 300 rpm
        "enc_pins": [], # no encoder
        "driver_pins": [21, 22], # pwm1, pwm2
    },
    "pololu_1": {
        "position": "rear left",
        "frequency": 300, # 300 rpm
        "enc_pins": [15,16], # encA, encB
        "driver_pins": [0, 7], # dir, en
    },
    "pololu_2": {
        "position": "front left",
        "frequency": 300, # 300 rpm
        "enc_pins": [1, 4], # encA, encB
        "driver_pins": [2, 3], # dir, en
    },
    "pololu_3": {
        "position": "rear right",
        "frequency": 300, # 300 rpm
        "enc_pins": [5, 6], # encA, encB
        "driver_pins": [30, 14], # dir, en
    },
    "pololu_4": {
        "position": "front right",
        "frequency": 300, # 300 rpm
        "enc_pins": [11, 31], # encA, encB
        "driver_pins": [12, 13], # dir, en
    },
    "actuonix_1": {
        "position": "veritcal left",
        "frequency": 300,   # hz
        "dc_low": 30,     # 30-60%
        "dc_high": 60,
        "stroke": 100,   # mm
    },
    "actuonix_2": {
        "position": "veritcal right",
        "frequency": 300,   # hz
        "dc_low": 30,     # 30-60%
        "dc_high": 60,
        "stroke": 100,   # mm
    },
    "actuonix_3": {
        "position": "horizontal left",
        "frequency": 300,   # hz
        "dc_low": 30,     # 30-60%
        "dc_high": 60,
        "stroke": 100,   # mm
    },
    # unused
    "actuonix_4": {
        "position": "horizontal right",
        "frequency": 300,   # hz
        "dc_low": 30,     # 30-60%
        "dc_high": 60,
        "stroke": 100,   # mm
    },
    # unused
    "turnigy_1": {
        "position": "plate left",
        "frequency": 300,   # hz
        "dc_low": 28,     # 28-64%
        "dc_high": 64,
    },
    # unused
    "turnigy_2": {
        "position": "plate right",
        "frequency": 300,   # hz
        "dc_low": 28,     # 28-64%
        "dc_high": 64,
    }
}