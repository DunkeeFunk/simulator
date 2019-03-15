# simulated data
from simulate_plants import Simulate
# machine learning stuff
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm

sim = Simulate("thing")
# bad data
baddictone = sim.sim_various_cold_temp_issues()
baddicttwo = sim.sim_various_light_issues()
baddicttre = sim.sim_various_humidity_issues()
baddictfor = sim.sim_various_soil_m_issues()
# good data
gooddictone = sim.good_situations()
gooddicttwo = sim.some_good_situations()
gooddicttre = sim.more_good_situations()
gooddictfor = sim.very_good_situations()

bad = pd.concat([baddictone["1"], baddictone["2"], baddictone["3"], baddictone["4"], baddictone["5"], baddictone["6"],
                 baddicttwo["1"], baddicttwo["2"], baddicttwo["3"], baddicttwo["4"], baddicttwo["5"], baddicttwo["6"],
                 baddicttre["1"], baddicttre["2"], baddicttre["3"], baddicttre["4"], baddicttre["5"], baddicttre["6"],
                 baddictfor["1"], baddictfor["2"], baddictfor["3"], baddictfor["4"], baddictfor["5"], baddictfor["6"]])

good = pd.concat([gooddictone["1"], gooddictone["2"], gooddictone["3"], gooddictone["4"], gooddictone["5"], gooddictone["6"],
                  gooddicttwo["1"], gooddicttwo["2"], gooddicttwo["3"], gooddicttwo["4"], gooddicttwo["5"], gooddicttwo["6"],
                  gooddicttre["1"], gooddicttre["2"], gooddicttre["3"], gooddicttre["4"], gooddicttre["5"], gooddicttre["6"],
                  gooddictfor["1"], gooddictfor["2"], gooddictfor["3"], gooddictfor["4"], gooddictfor["5"], gooddictfor["6"]])

bad = bad.reset_index(drop=True)
good = good.reset_index(drop=True)
# merge
data = pd.concat([bad, good])
data = data.reset_index(drop=True)
# need a nice shape
X = np.array(data.drop(['soil_m'], 1))
y = np.array(data[["temp", "humidity", "light", "condition"]])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = svm.SVC()
# bad shape error it wants two arrays of the same size, my eyes are sore come back to this later
clf.fit(X_train, y_train)

accur = clf.score(X_test,y_test)



















