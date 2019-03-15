import numpy as np


'''
Class for simulating temperature data. 
Quarters : temperatures at 12am, 6am, 12pm, 6pm 
Examples - first_q = 6.7, second_q = 5.6, third_q = 8.2, fourth_q = 8.1
this is an ex from March, this is bad conditions, my plants are not happy. 
noise is added with a random distribution
single quarter is 24 because we take measurements every 15 mins, there are 
96, 15 min intervals in one day so divide that by 4 gives you 24
condition has not been uses yet but when we return DataFrames it will
'''


class TempSimulator:
    def __init__(self, t_quarters):
        # quarters
        self.t_quarters = t_quarters
        self.data_dictionary = {}
        self.single_q = 24

    def temperature_data_generator(self):
        # one day in march between 12 at night and 6am
        q_one_array = np.linspace(start=self.t_quarters[0], stop=self.t_quarters[1], num=self.single_q)
        # one day in march between 6am and 12pm
        q_two_array = np.linspace(start=self.t_quarters[1], stop=self.t_quarters[2], num=self.single_q)
        # one day in march between 12pm and 6pm
        q_three_array = np.linspace(start=self.t_quarters[2], stop=self.t_quarters[3], num=self.single_q)
        # one day in march between 6pm and 12am
        q_four_array = np.linspace(start=self.t_quarters[3], stop=self.t_quarters[0], num=self.single_q)

        # one full day
        one_full_day = np.concatenate((q_one_array, q_two_array, q_three_array, q_four_array), axis=None)
        # adding randomisation
        noise = np.random.normal(0, 0.4, 96)
        one_full_day = noise + one_full_day

        return one_full_day


