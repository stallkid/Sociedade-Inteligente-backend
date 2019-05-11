from sklearn import svm

class SupportVectorMachine():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def train(self):
        svm_clf = svm.SVC(kernel='linear')
        svm_clf.fit(self.x, self.y)

