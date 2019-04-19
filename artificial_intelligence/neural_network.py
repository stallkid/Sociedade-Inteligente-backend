import sklearn as sk
from sklearn.neural_network import MLPClassifier
import pandas as pd
import os

class NeuralNetworkIA():

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

    def neural_network(self):
        df = pd.DataFrame(self.rows, columns=self.cols)

        y = df.iloc[:,(len(self.cols)-1)]
        X = df.iloc[:,:(len(self.cols)-1)]

        NN = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(1,1), random_state=1)
        NN.fit(X, y)
        NN.predict(X.iloc[(len(self.rows)-1):,:])
        return round(NN.score(X, y), 4)
