#!/usr/bin/env python3

import pickle
import os
import glob
import re
import numpy as np

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

def extract_eeg():
    data = []

    """
    Columns: TimeStamp,
    Delta_TP9,Delta_AF7,Delta_AF8,Delta_TP10,Theta_TP9,Theta_AF7,Theta_AF8,Theta_TP10,Alpha_TP9,Alpha_AF7,Alpha_AF8,Alpha_TP10,Beta_TP9,Beta_AF7,Beta_AF8,Beta_TP10,Gamma_TP9,Gamma_AF7,Gamma_AF8,Gamma_TP10,
    RAW_TP9,RAW_AF7,RAW_AF8,RAW_TP10,
    AUX_RIGHT,Accelerometer_X,Accelerometer_Y,Accelerometer_Z,Gyro_X,Gyro_Y,Gyro_Z,
    HeadBandOn,HSI_TP9,HSI_AF7,HSI_AF8,HSI_TP10,Battery 
    """

    for user_dir in glob.glob("./probes/*"):
        if not os.path.exists(f"{user_dir}/probe"):
            # not a valid eeg folder
            continue

        with open(f"{user_dir}/probe", "r") as f:
            sents = [x.strip().split("\t") for x in f.readlines()]
        
        eeg_files = glob.glob(f"{user_dir}/*.eeg")
        usernames = [re.findall(r"/P\d{2}", eeg_file) for eeg_file in eeg_files]
        usernames = {x[0][1:] for x in usernames if len(x) > 0}

        for username in usernames:
            # is ordered
            files = [glob.glob(f"{user_dir}/{username}-{i:02}*.eeg") for i in range(32)]
            files = [f[0] for f in files if len(f) > 0 and os.path.exists(f[0])]

            for f, sent in zip(files, sents):
                with open(f, "r") as f:
                    data_eeg = [x.strip().split(",") for x in f.readlines()]
                    if len(data_eeg) == 0:
                        print("skipping empty EEG", user_dir, username)
                        continue
                    dates = [line[0] for line in data_eeg]
                    data_eeg = [
                        [float(x) for x in line[1:] if "/muse/elements/" not in line[-1]]
                        for line in data_eeg
                    ]
                    data_eeg = [
                        line for line in data_eeg
                        if len(line) != 0
                    ]
                    data.append({"dates": dates, "user": username, "eeg": data_eeg, "sent": sent})

    return data

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

def argmax_n(a, n):
    return np.argpartition(a, -n)[-n:]

def argmin_n(a, n):
    return np.argpartition(a, -n)[:n]
