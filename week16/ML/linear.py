import numpy as np

class LinearRegression():
    def __init__(self):
        self.a_ = None
        self.b_=None
    def fit(self,x_train,y_train):
        assert len(x_train) ==len(y_train),"长度需要相同"
        assert x_train.ndim ==1 ,"只支持一个特征"
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)
        u,v = 0,0
        for x_i, y_i in zip(x_train, y_train):
            u += (x_i - x_mean) * (y_i - y_mean)
            v += (x_i - x_mean) ** 2

        self.a_ = u / v
        self.b_ = y_mean - self.a_ * x_mean
        return self


    def predict(self,x_predict):
        assert self.a_ is not None,"请先fit"
        assert x_predict.ndim ==1,"只支持一个特征"
        return np.array([self.a_*x+self.b_ for x in x_predict])

