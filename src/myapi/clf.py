import pickle

class Predictor():

    def __init__(self, pickle_path):
        with open(pickle_path,'rb') as file:
            self.knn = pickle.load(file)

    def predict(self, features):
        return self.knn.predict(features)