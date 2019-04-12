# simulated data
from simulate_plants import Simulate
# machine learning stuff
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


class MLWrapper:
    def __init__(self):
        '''
        flow of events
        1.) call wrangle data function to simulate all data and wrangle it into the appropriate shape
        2.) call train test split function to split data into training and testing segments
        3.) call the model trainer to train all models and dump them into pickles
        4.) classify data with one of the classify functions provided
        '''
        # instance of simulate class see wrangle data function for usage
        self.sim = Simulate("thing")
        # save the models in pickles
        self.knn_filename = 'knnmodel.sav'
        self.svm_filename = 'svmmodel.sav'
        self.rf_filename = 'rfmodel.sav'
        self.X_train = 0
        self.X_test = 0
        self.y_train = 0
        self.y_test = 0
        self.data = 0
        self.X = 0
        self.y = 0

    def wrangle_data(self):
        # bad data
        baddictone = self.sim.sim_various_cold_temp_issues()
        baddicttwo = self.sim.sim_various_light_issues()
        baddicttre = self.sim.sim_various_humidity_issues()
        baddictfor = self.sim.sim_various_soil_m_issues()
        # good data
        gooddictone = self.sim.good_situations()
        gooddicttwo = self.sim.some_good_situations()
        gooddicttre = self.sim.more_good_situations()
        gooddictfor = self.sim.very_good_situations()
        # wrap all the data up
        bad = pd.concat(
            [baddictone["1"], baddictone["2"], baddictone["3"], baddictone["4"], baddictone["5"], baddictone["6"],
             baddicttwo["1"], baddicttwo["2"], baddicttwo["3"], baddicttwo["4"], baddicttwo["5"], baddicttwo["6"],
             baddicttre["1"], baddicttre["2"], baddicttre["3"], baddicttre["4"], baddicttre["5"], baddicttre["6"],
             baddictfor["1"], baddictfor["2"], baddictfor["3"], baddictfor["4"], baddictfor["5"], baddictfor["6"]])

        good = pd.concat(
            [gooddictone["1"], gooddictone["2"], gooddictone["3"], gooddictone["4"], gooddictone["5"], gooddictone["6"],
             gooddicttwo["1"], gooddicttwo["2"], gooddicttwo["3"], gooddicttwo["4"], gooddicttwo["5"], gooddicttwo["6"],
             gooddicttre["1"], gooddicttre["2"], gooddicttre["3"], gooddicttre["4"], gooddicttre["5"], gooddicttre["6"],
             gooddictfor["1"], gooddictfor["2"], gooddictfor["3"], gooddictfor["4"], gooddictfor["5"],
             gooddictfor["6"]])
        # sort the indexes out
        bad = bad.reset_index(drop=True)
        good = good.reset_index(drop=True)
        # merge
        self.data = pd.concat([bad, good])
        # set the indexes again after the merge
        self.data = self.data.reset_index(drop=True)
        # X and Y for machine learning algorithms
        self.X = np.array(self.data[['temp', 'humidity', 'light']])
        self.y = np.array(self.data[['soil_m']])

    def _train_test_split(self):
        # 80 20 train test split, maybe pass the split as a param in later work
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2)

    def model_trainer(self):
        self._train_test_split()
        # give me an instance of KNN classifier
        neigh = KNeighborsClassifier()
        # fit it with the data generated on instantiation
        neigh.fit(self.X_train, self.y_train)
        # give me an instance of SVM classifier
        clf = svm.SVC()
        # fit the training data
        clf.fit(self.X_train, self.y_train)
        # same
        rf_clf = RandomForestClassifier()
        rf_clf.fit(self.X_train, self.y_train)
        # pickle the models aka save
        pickle.dump(neigh, open(self.knn_filename, 'wb'))
        pickle.dump(clf, open(self.svm_filename, 'wb'))
        pickle.dump(rf_clf, open(self.rf_filename, 'wb'))

    def knn_classify(self, temperature, humidity, light):
        loaded_knn_model = pickle.load(open(self.knn_filename, 'rb'))
        # score it, be aware of double return statements
        accur = loaded_knn_model.score(self.X_test, self.y_test)
        # predict
        knn_single_predic = loaded_knn_model.predict(np.array([[temperature, humidity, light]]))
        # return the prediction and its accuracy
        return knn_single_predic[0], accur

    def svm_classify(self, temp, hum, light_mea):
        # load the model from a pickle
        loaded_svm_model = pickle.load(open(self.svm_filename, 'rb'))
        # score the model for accuracy
        accuracy = loaded_svm_model.score(self.X_test, self.y_test)
        # make the prediction
        svm_single_prediction = loaded_svm_model.predict(np.array([[temp, hum, light_mea]]))
        # return prediction and accuracy
        return svm_single_prediction[0], accuracy

    def random_forrest_classify(self, tmp, humid, light_m):
        loaded_rf_model = pickle.load(open(self.rf_filename, 'rb'))
        a = loaded_rf_model.score(self.X_test, self.y_test)
        rf_single_prediction = loaded_rf_model.predict(np.array([[tmp, humid, light_m]]))
        return rf_single_prediction[0], a

'''
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
X = np.array(data[['temp', 'humidity', 'light']])  # try this
# X = np.array(data[['temp', 'humidity', 'light', 'condition']])
# y = np.array(data[['soil_m']]).reshape((1, int(data[['soil_m']].size)))
y = np.array(data[['soil_m']])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# need to make the data go across the ways not down the way
# y_train = y_train.reshape((1, int(y_train.size)))
# try this one out for banter
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)
# clf = svm.SVC()
# bad shape error it wants two arrays of the same size, my eyes are sore come back to this later
# clf.fit(X_train, y_train)

# lets try this prediction out
y_pred = neigh.predict(X_test)
# lets try get some accuracy
accur = neigh.score(X_test, y_test)
print(accur)
one_single_predic = neigh.predict(np.array([[6.07, 64.54, False]]))
print(one_single_predic)

'''

















