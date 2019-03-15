import numpy as np


class SoilMSimulator:
    def __init__(self, soilmopen, soilmclose):
        self.soilmopen = soilmopen
        self.soilmclose = soilmclose
        self.data_dictionary = {}

    def soil_data_generator(self):
        fancy = np.arange(1, 97)
        one_day_soilm = (fancy > self.soilmopen) & (fancy < self.soilmclose)  # the numpy docs actually calls this
        return one_day_soilm                                           # fancy indexing LOL
