import sklearn as sk
from sklearn.linear_model import LogisticRegression
import pandas as pd
import os

class LogisticRegressionIA():

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

    def logistic_regression(self):
        df = pd.DataFrame(self.rows, columns=self.cols)

        y = df.iloc[:,1]
        X = df.iloc[:,:1]

        LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(X,y)
        LR.predict(X.iloc[2:,:])

        return round(LR.score(X,y), 4)
