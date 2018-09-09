import numpy as np
from .knn import kNN_classify
from .metrics import accuracy_score
from .model_selection import train_test_split
import matplotlib.pyplot as plt
from collections import Counter
from collections import Counter
from .metrics import accuracy_score


def gini(y):
    counter = Counter(y)
    result = 0
    for v in counter.values():
        result += (v / len(y)) ** 2
    return 1 - result


def cut(X, y, d, v):
    ind_left = (X[:, d] <= v)
    #     print(ind_left)
    ind_right = (X[:, d] >= v)
    return X[ind_left], X[ind_right], y[ind_left], y[ind_right]


def try_split(X, y):
    best_g = 1
    best_d = -1
    best_v = -1
    for d in range(X.shape[1]):
        sorted_index = np.argsort(X[:, d])
        #         print(sorted_index)
        for i in range(len(X) - 1):
            if X[sorted_index[i], d] == X[sorted_index[i + 1], d]:
                continue
            v = (X[sorted_index[i], d] + X[sorted_index[i + 1], d]) / 2
            #             print("d={}, v={}".format(d,v))
            X_left, X_right, y_left, y_right = cut(X, y, d, v)
            g_all = gini(y_left) + gini(y_right)

            if g_all < best_g:
                best_g = g_all
                best_d = d
                best_v = v
    return best_d, best_v, best_g

'''
决策树
'''
class DecisionTreeClassfiy():
    def __init__(self):
        self.tree_ = None

    # 拟合训练数据
    def fit(self,X,y):
        self.tree_ = self.create_tree(X,y)
        return self

    # 数据预测
    def predict(self,X):
        assert self.tree_ is not None,"请先调用fit方法"
        return np.array([self._predict(x,self.tree_) for x in X])

    # 单个样本预测
    def _predict(self,x,node):
        if node.label is not None:
            return node.label
        if x[node.dim] <= node.value:
            return self._predict(x,node.children_left)
        else:
            return self._predict(x,node.children_right)


    # 创建决策树
    def create_tree(self,X, y):
        d, v, g = try_split(X, y)
        if d == -1 or g == 0:
            return None
        node = Node(d, v, g)  # 根节点

        X_left, X_right, y_left, y_right = cut(X, y, d, v)

        node.children_left = self.create_tree(X_left, y_left)
        if node.children_left is None:
            label = Counter(y_left).most_common(1)[0][0]
            node.children_left = Node(l=label)

        node.children_right = self.create_tree(X_right, y_right)
        if node.children_right is None:
            label = Counter(y_right).most_common(1)[0][0]
            node.children_right = Node(l=label)

        return node
    # 分类准确度测量
    def score(self,X_test,y_test):
        y_predict = self.predict(X_test)
        return accuracy_score(y_test,y_predict)
class Node():
    def __init__(self,d= None,v= None,g= None,l= None):
        self.dim = d
        self.value = v
        self.gini =g
        self.label =l
        self.children_left = None
        self.children_right = None
    def __repr__(self):
        return 'Node(d={},v={},g={},l={})'.format(self.dim,self.value,self.gini,self.label)