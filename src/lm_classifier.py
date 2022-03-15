#!/usr/bin/env python3

from utils import extract_amb_namb, save_pickle, read_pickle
from embd import BertWrap, SentenceBertWrap
from sklearn.linear_model import LogisticRegression
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split, cross_validate
import numpy as np
import random

amb, namb = extract_amb_namb()

# model = SentenceBertWrap()
# amb = [model.embd(s, "avg") for s in tqdm(amb)]
# namb = [model.embd(s, "avg") for s in tqdm(namb)]
# save_pickle("computed/sbert_avg.pkl", (amb, namb))

amb, namb = read_pickle("computed/sbert_cls.pkl")

data_x = amb + namb
data_x = StandardScaler().fit_transform(data_x)
data_y = [1]*len(amb) + [0]*len(namb)
print(len(amb), len(namb), len(data_x))

# data = list(zip(data_x, data_y))
# random.shuffle(data)
# data_x, data_y = zip(*data)

# model = LogisticRegression()
result = cross_validate(
    LogisticRegression(C=0.3),
    data_x, data_y,
    cv=10,
    return_train_score=True
)
# model.cvfit(data_x, data_y)
# acc = model.score(data_x, data_y)
print("train acc", np.average(result["train_score"]))
print("test acc ", np.average(result["test_score"]))