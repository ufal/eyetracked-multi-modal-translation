#!/usr/bin/env python3

from utils import extract_amb_namb, save_pickle, read_pickle

amb, namb = extract_amb_namb()


print("\n".join(amb))