import numpy as np
import random

''' 
this code is all wrong and more of a sandbox for me to try things out in.
Excuse the ignorance, I was trying to randomise the data. It was wrote before i found out 
how to add noise with a normal dist 
'''
#  Weather Assumption's
first_q = 6.7
second_q = 5.6
third_q = 8.2
fourth_q = 8.1
# 24 measurements in a quarter
single_quarter = int(96 / 4)

# one day in march between 12 at night and 6am
qonearray = np.linspace(start=first_q, stop=second_q, num=single_quarter)
# looping to add some random noise like sonya said
for i in range(0, 24):
    rand_sd = random.uniform(-0.3, 0.1)
    qonearray[i] = qonearray[i] + rand_sd

# one day in march between 6am and 12pm
qtwoarray = np.linspace(start=second_q, stop=third_q, num=single_quarter)
for i in range(0, 24):
    rand_sd = random.uniform(-0.2, 0.8)
    qtwoarray[i] = qtwoarray[i] + rand_sd

# one day in march between 12pm and 6pm
qthreearray = np.linspace(start=third_q, stop=fourth_q, num=single_quarter)
for i in range(0, 24):
    rand_sd = random.uniform(-0.0, 0.8)
    qthreearray[i] = qthreearray[i] + rand_sd

# one day in march between 6pm and 12am
qfourarray = np.linspace(start=fourth_q, stop=first_q, num=single_quarter)
for i in range(0, 24):
    rand_sd = random.uniform(-0.5, 0.2)
    qfourarray[i] = qfourarray[i] + rand_sd

# one full day
one_full_day = np.concatenate((qonearray, qtwoarray, qthreearray, qfourarray), axis=None)
# lets start pulling out some samples - decrement the mean to get worse conditions
# sample_one = np.random.normal(np.mean(one_full_day), np.std(one_full_day), one_full_day.size)

from datetime import datetime, timedelta


def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta


dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in
       datetime_range(datetime(2018, 3, 7, 12), datetime(2018, 3, 8, 12),
       timedelta(minutes=15))]

import matplotlib.pyplot as plt

X = dts
plt.plot(X, one_full_day)
plt.xticks(X, X, rotation='vertical')
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
plt.ylabel('Temp')
plt.show()



