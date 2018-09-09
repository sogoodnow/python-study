import numpy as np
from collections import Counter

from .metrics import accuracy_score


class KNeighborsClassifier():
    def __init__(self,k=5,p=2):
        assert k > 0, 'k要大于0'
        assert p > 0, 'p要大于0'
        self.k = k
        self.p= p
        self._X_train = None
        self._y_train =None

    def fit(self,X_train,y_train):
        assert X_train.shape[0] == y_train.shape[0], '样本数量要相同'
        assert self.k <= y_train.shape[0], 'k小于等于总样本数'
        self._X_train =X_train
        self._y_train =y_train
        return self

    def predict(self,X_predict):
        return np.array([self._predict(x) for x in X_predict])

    def _predict(self,x):
        distances = [distance(item, x, p=self.p) for item in self._X_train]
        nearest = np.argsort(distances)[:self.k]
        k_labels = self._y_train[nearest]

        return Counter(k_labels).most_common(1)[0][0]

    # 分类准确度测量
    def score(self,X_test,y_test):
        y_predict = self.predict(X_test)
        return accuracy_score(y_test,y_predict)

def kNN_classify(X_train,y_train,X_predict,k=5,p=2):

    assert k > 0, 'k要大于0'
    assert k <= y_train.shape[0], 'k小于等于总样本数'
    assert p>0 ,'p要大于0'
    assert X_train.shape[0]==y_train.shape[0],'样本数量要相同'
    assert X_train.shape[1]==X_predict.shape[1],'样本数量要相同'

    return np.array([_predict(X_train,y_train,x,k,p) for x in X_predict])


def _predict(X_train,y_train,x,k,p):
    distances = [distance(item,x,p) for item in X_train]
    nearest = np.argsort(distances)[:k]
    k_labels = y_train[nearest]

    return Counter(k_labels).most_common(1)[0][0]

def distance(a,b,p=2):
    return np.sum(np.abs(a-b)**p)**(1/p)