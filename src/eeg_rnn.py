#!/usr/bin/env python3

from utils import save_pickle, read_pickle, argmax_n, argmin_n
import numpy as np
from numpy.fft import fft
from rnn_model import LSTMModel
from sklearn.svm import SVC
import random
import torch

def reduce_line(line):
    label = line["sent"][0] == "amb"
    # select only relevant attributes
    eeg = np.array(line["eeg"]).T[0:20,:].T
    # it's already FFT'd
    # out = np.array([
    #     np.concatenate([
    #         fft(line)[:10] for line in
    #         eeg[:,i*100:(i+1)*100]
    #     ])
    #     for i in range(eeg.shape[1]//100)
    # ])
    # print(out.shape)

    return (torch.Tensor(eeg), label*1)
    
data = read_pickle("computed/eeg.pkl")
data = [reduce_line(line) for line in data]
# random.shuffle(data)
data_x, data_y = zip(*data)


# data_x = StandardScaler().fit_transform(data_x)
# data = list(zip(data_x, data_y))

# print(data_x[0].shape, "x shape")
# print(len(data), "total")
# print(len([x for x in data_y if x == 1]), "amb")
# print(len([x for x in data_y if x == 0]), "namb")

model = LSTMModel()
model.train_loop(data[:-100], data[-100:])