import numpy as np


class LightSimulator:
    def __init__(self, sunup, sundown):
        # good, bad
        self.sunup = sunup
        self.sundown = sundown
        self.data_dictionary = {}

    def light_data_generator(self):
        fancy = np.arange(1, 97)
        one_day_light = (fancy > self.sunup) & (fancy < self.sundown)  # the numpy docs actually calls this
        return one_day_light                                           # fancy indexing LOL
