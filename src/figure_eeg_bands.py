#!/usr/bin/env python3

from utils import save_pickle, read_pickle
import numpy as np
import matplotlib.pyplot as plt
import random

data = read_pickle("computed/eeg_small.pkl")

COLORS = ["tab:blue", "tab:red", "tab:green", "tab:brown"]
ALPHAS = [1.0, 0.8, 0.6, 0.4, 0.2]
LABELS_NODE = ["TP9", "AF7", "AF8", "TP10"]
LABELS_BAND = ["Delta", "Theta", "Alpha", "Beta", "Gamma"]

print(len(data))
total_count = len([x[0 + 20] for x in data[92]["eeg"]])

for node_i in range(0, 2):
    for band_i in range(0, 5):
        plt.plot(
            np.linspace(0, total_count/4, num=total_count),
            [x[band_i * 4 + node_i] for x in data[92]["eeg"]],
            color=COLORS[node_i],
            alpha=ALPHAS[band_i],
            label=LABELS_NODE[node_i] + " " + LABELS_BAND[band_i],
            linewidth=1,
        )
plt.legend(
    loc="upper right",
    ncol=2,
)
plt.ylabel("dB")
ax = plt.gca()
ax.yaxis.labelpad = -10
plt.xlabel("Stage duration (ms)")
plt.tight_layout(pad=0.2)
plt.savefig("figures/eeg_bands.pdf")
plt.show()