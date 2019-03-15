import numpy as np

# Example Humidity Assumptions
quarter_one = 78.0
quarter_two = 94.0
quarter_three = 60.0
quarter_four = 76.0

'''
Class for simulating temperature data. 
Quarters : temperatures at 12am, 6am, 12pm, 6pm 
Examples - first_q = 78, second_q = 94, third_q = 60, fourth_q = 76
'''


class HumiditySimulator:
    def __init__(self, h_quarters):
        # quarters
        self.h_quarters = h_quarters
        self.data_dictionary = {}
        self.single_q = 24

    def humidity_data_generator(self):
        # one day in march between 12 at night and 6am
        q_one_array = np.linspace(start=self.h_quarters[0], stop=self.h_quarters[1], num=self.single_q)
        # one day in march between 6am and 12pm
        q_two_array = np.linspace(start=self.h_quarters[1], stop=self.h_quarters[2], num=self.single_q)
        # one day in march between 12pm and 6pm
        q_three_array = np.linspace(start=self.h_quarters[2], stop=self.h_quarters[3], num=self.single_q)
        # one day in march between 6pm and 12am
        q_four_array = np.linspace(start=self.h_quarters[3], stop=self.h_quarters[0], num=self.single_q)

        # one full day
        one_full_day = np.concatenate((q_one_array, q_two_array, q_three_array, q_four_array), axis=None)
        # adding randomness   mean std bins
        noise = np.random.normal(0, 1.5, 96)
        one_full_day = one_full_day + noise

        return one_full_day

























