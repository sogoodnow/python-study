
def accuracy_score(y, y_predict):
    assert y.shape[0] == y_predict.shape[0],"y y_predict长度需要相同"
    return sum(y == y_predict) / len(y)
