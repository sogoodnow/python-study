import numpy as np
from collections import Counter


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