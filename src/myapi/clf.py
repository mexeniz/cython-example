import pickle

from sklearn.neighbors import KNeighborsClassifier

class Predictor():

    def __init__(self, pickle_path):
        with open(pickle_path,'rb') as file:
            knn = pickle.load(file)
            if not isinstance(knn, KNeighborsClassifier):
                raise Exception('Pickled model is not KNN.')
            self.knn = knn

    def predict(self, features):
        return self.knn.predict(features)