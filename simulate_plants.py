from hum_sim import HumiditySimulator
from simulator import TempSimulator
from light_sim import LightSimulator
from soil_m_sim import SoilMSimulator

import pandas as pd
import numpy as np


class Simulate:
    def __init__(self, thing):
        self.thing = thing

    def oneday(self, temp_quarters, humid_qs, soil_from, soil_to, light_from, light_to, condition):
        '''
            example data of one bad day in march
            condition = "bad"
            temp_dev = [0.2, 0.3, 0.2, 0.3] no longer required - noise added
            temp_quarters = [6.7, 5.6, 8.2, 8.1]
            humid_dev = [5, 3, 2, 4]
            humid_qs = [78.0, 94.0, 60.0, 76.0]
            soil_from = 0
            soil_to = 97
            light_from = 24
            light_to = 76
        '''

        # find a better way to wrap this up later - temp data simd
        temp_sim = TempSimulator(temp_quarters)
        temp_day = temp_sim.temperature_data_generator()

        # humidity data sim
        hum_sim = HumiditySimulator(humid_qs)
        humid_day = hum_sim.humidity_data_generator()

        # soil moisture data
        soil_sim = SoilMSimulator(soil_from, soil_to)
        soil_day = soil_sim.soil_data_generator()

        # light day
        light_sim = LightSimulator(light_from, light_to)
        light_day = light_sim.light_data_generator()

        condition_array = np.full(96, condition)

        # wrap it up in a dict and throw it into a df
        d = {
            "id": range(96),
            'temp': temp_day,
            "humidity": humid_day,
            "soil_m": soil_day,
            "light": light_day,
            "condition": condition_array
        }

        return pd.DataFrame(data=d)

    def sim_various_cold_temp_issues(self):
        # plants need above 12 degrees heat so all these temps are bad and simulate temps in march
        # top 3 are bad humidity, bottom 3 are decent humidity, plants need between 80 and 90 percent daytime humidity
        data_dict = {
            "1": self.oneday([6.6, 5.6, 8.2, 8.1], [65.0, 75.0, 79.0, 75.0], 0, 0, 72, 80, 1),
            "2": self.oneday([4.7, 5.6, 7.2, 6.1], [52.0, 70.0, 78.0, 70.0], 24, 97, 60, 75, 1),
            "3": self.oneday([2.7, 4.6, 8.2, 7.1], [50.0, 72.0, 77.0, 71.0], 10, 97, 24, 72, 1),
            "4": self.oneday([5.1, 3.6, 8.2, 6.2], [55.0, 83.0, 89.0, 68.0], 0, 97, 24, 72, 1),
            "5": self.oneday([4.1, 4.6, 8.1, 7.2], [66.0, 82.0, 88.0, 70.0], 0, 0, 24, 72, 1),
            "6": self.oneday([3.1, 4.6, 8.1, 7.2], [69.0, 87.0, 89.0, 71.0], 0, 0, 24, 72, 1)
        }

        return data_dict

    def sim_various_humidity_issues(self):
        # 2 - simulates temp being too hot for plants
        data_dict = {
            "1": self.oneday([18.0, 13.6, 22.2, 19.1], [45.0, 35.0, 69.0, 75.0], 0, 0, 25, 54, 1),
            "2": self.oneday([25.7, 20.6, 35.2, 30.1], [32.0, 20.0, 79.0, 69.0], 0, 97, 24, 30, 1),
            "3": self.oneday([16.7, 13.6, 25.2, 18.1], [50.0, 42.0, 47.0, 71.0], 10, 97, 26, 35, 1),
            "4": self.oneday([5.1, 3.6, 8.2, 6.2], [51.0, 60.0, 65.0, 49.0], 0, 0, 24, 72, 1),
            "5": self.oneday([4.1, 4.6, 8.1, 7.2], [66.0, 72.0, 73.0, 68.0], 0, 97, 24, 76, 1),
            "6": self.oneday([17.1, 13.6, 26.1, 17.2], [49.0, 61.0, 60.0, 20.0], 0, 0, 24, 72, 1)
        }

        return data_dict

    def sim_various_soil_m_issues(self):
        data_dict = {
            "1": self.oneday([4.1, 2.6, 8.1, 5.2], [45.0, 35.0, 69.0, 75.0], 0, 0, 25, 32, 1),
            "2": self.oneday([17.1, 13.1, 26.1, 14.2], [32.0, 20.0, 79.0, 69.0], 0, 97, 24, 30, 1),
            "3": self.oneday([4.1, 1.6, 7.1, 5.2], [69.0, 87.0, 89.0, 71.0], 10, 97, 26, 56, 1),
            "4": self.oneday([16.7, 13.6, 25.2, 18.1], [51.0, 60.0, 65.0, 49.0], 0, 0, 24, 72, 1),
            "5": self.oneday([1.1, 0.6, 8.1, 7.2], [66.0, 72.0, 73.0, 68.0], 0, 97, 24, 76, 1),
            "6": self.oneday([4.1, 2.6, 10.1, 7.2], [69.0, 87.0, 90.0, 70.0], 0, 0, 24, 25, 1)
        }

        return data_dict

    def sim_various_light_issues(self):
        data_dict = {
            "1": self.oneday([4.1, 1.6, 8.1, 5.2], [45.0, 35.0, 69.0, 75.0], 0, 0, 25, 26, 1),
            "2": self.oneday([1.1, 0.6, 8.1, 7.2], [32.0, 20.0, 79.0, 69.0], 0, 97, 24, 42, 1),
            "3": self.oneday([4.1, 1.6, 10.1, 3.2], [89.0, 81.0, 89.0, 71.0], 10, 97, 26, 35, 1),
            "4": self.oneday([16.7, 13.6, 25.2, 18.1], [60.0, 51.0, 65.0, 49.0], 0, 97, 24, 30, 1),
            "5": self.oneday([1.1, 0.6, 8.1, 7.2], [69.0, 87.0, 89.0, 71.0], 0, 1, 24, 25, 1),
            "6": self.oneday([16.7, 13.6, 25.2, 18.1], [51.0, 60.0, 65.0, 49.0], 0, 1, 24, 40, 1)
        }

        return data_dict

    def good_situations(self):
        data_dict = {
            "1": self.oneday([17.1, 13.9, 25.2, 19.2], [70.0, 68.0, 85.0, 80.0], 0, 97, 24, 72, 3),
            "2": self.oneday([17.5, 13.6, 26.4, 21.2], [70.0, 65.0, 86.0, 79.0], 0, 97, 24, 72, 3),
            "3": self.oneday([17.8, 13.9, 27.6, 22.2], [70.0, 66.0, 87.0, 81.0], 10, 97, 26, 25, 3),
            "4": self.oneday([17.9, 13.7, 28.8, 17.2], [70.0, 67.0, 88.0, 82.0], 10, 97, 24, 73, 3),
            "5": self.oneday([17.7, 13.3, 29.1, 19.2], [70.0, 66.0, 89.0, 83.0], 0, 97, 24, 75, 3),
            "6": self.oneday([17.2, 13.2, 25.5, 20.2], [70.0, 68.0, 82.0, 84.0], 0, 97, 24, 74, 3)
        }

        return data_dict


sim = Simulate("thing")
temp_issues = sim.sim_various_cold_temp_issues()
