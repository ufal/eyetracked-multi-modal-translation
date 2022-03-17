#!/usr/bin/env python3

from utils import save_pickle, read_pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
from sklearn.svm import SVC
import random

def reduce_line(line):
    label = line["sent"][0] == "amb"
    pivot = len(line["eeg"])//2
    x1 = np.average(np.array(line["eeg"][0*pivot:1*pivot]), axis=0)
    x2 = np.average(np.array(line["eeg"][1*pivot:2*pivot]), axis=0)
    x = np.concatenate((x1, x2))
    return (x, label)
    
data = read_pickle("computed/eeg.pkl")
data = [reduce_line(line) for line in data]
# random.shuffle(data)
data_x, data_y = zip(*data)

data_x = StandardScaler().fit_transform(data_x)

print(data_x[0].shape, "x shape")
print(len(data), "total")
print(len([x for x in data_y if x == 1]), "amb")
print(len([x for x in data_y if x == 0]), "namb")

model = LogisticRegression(max_iter=1000)
# model = SVC()
# model.fit(data_x[:-100], data_y[:-100])
result = cross_validate(model, data_x, data_y, cv=10, n_jobs=4, return_train_score=True)
# train_acc = model.score(data_x[:-100], data_y[:-100])
print(f"train acc: {np.average(result['train_score']):.2%}%")
print(f"dev acc:  {np.average(result['test_score']):.2%}%")