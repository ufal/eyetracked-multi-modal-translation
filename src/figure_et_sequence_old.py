#!/usr/bin/env python3

from utils import save_pickle, read_pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import random

data = read_pickle("computed/et_small.pkl")

COLORS = ["tab:blue", "tab:red", "tab:green", "tab:brown"]
ALPHAS = [0.8, 0.6, 0.4, 0.2]
LABELS_NODE = ["TP9", "AF7", "AF8", "TP10"]

cm = plt.get_cmap("viridis")

for line_i, line in enumerate(data[0]):
    if line_i % 100 != 0:
        continue
    x = line[1]
    y = line[2]
    plt.scatter(
        x, y,
        color=cm(line_i/len(data[0]))
    )

# plt.ylim(top=1250)
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.tight_layout(pad=0.2)
# plt.savefig("figures/et_sequence.pdf")
plt.show()
