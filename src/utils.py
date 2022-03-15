#!/usr/bin/env python3

import pickle

def extract_amb_namb():
    import glob

    amb = []
    namb = []

    for file in glob.glob("./probes/*/probe"):
        with open(file, "r") as f:
            sents = [x.strip().split("\t") for x in f.readlines()]
            for s in sents:
                if s[0] == "amb":
                    amb.append(s[3])
                elif s[0] == "namb":
                    namb.append(s[3])
                else:
                    raise Exception("Unknown marker", s[0])

    # remove duplicates
    return list(set(amb)), list(set(namb))

def get_device():
    import torch
    if torch.cuda.is_available():
        return torch.device("cuda:0")
    else:
        return torch.device("cpu")

def read_pickle(path):
    with open(path, "rb") as fread:
        reader = pickle.Unpickler(fread)
        return reader.load()

def save_pickle(path, data):
    with open(path, "wb") as fwrite:
        pickler = pickle.Pickler(fwrite)
        pickler.dump(data)