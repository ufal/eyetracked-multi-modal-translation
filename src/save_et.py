#!/usr/bin/env python3

from utils import extract_et, save_pickle, read_pickle

data = extract_et(count=100)

# save_pickle("computed/et.pkl", data)

# data = data[:100]
save_pickle("computed/et_small.pkl", data)