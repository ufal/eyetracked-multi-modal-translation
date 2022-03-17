#!/usr/bin/env python3

from utils import extract_eeg, save_pickle, read_pickle

data = extract_eeg()

save_pickle("computed/eeg.pkl", data)

print(data[0].keys())
print(len(data))

data = data[:100]
save_pickle("computed/eeg_small.pkl", data)