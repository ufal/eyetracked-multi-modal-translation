#!/usr/bin/env python3

from utils import save_pickle, read_pickle
import numpy as np
import matplotlib.pyplot as plt
import random

data = read_pickle("computed/eeg_small.pkl")

COLORS = ["tab:blue", "tab:red", "tab:green", "tab:brown"]
ALPHAS = [0.8, 0.6, 0.4, 0.2]
LABELS_NODE = ["TP9", "AF7", "AF8", "TP10"]

print(len(data))

total_count = len([x[0 + 20] for x in data[92]["eeg"]])

for node_i in range(0, 4):
    plt.plot(
        np.linspace(0, total_count/4, num=total_count),
        np.array([x[node_i + 20] for x in data[92]["eeg"]]) + 100 * node_i,
        color=COLORS[node_i],
        alpha=0.5,
        label=LABELS_NODE[node_i],
        linewidth=0.4,
    )
plt.legend(
    loc="upper right",
    ncol=4,
)

plt.ylim(top=1250)
ax = plt.gca()
ax.get_yaxis().set_visible(False)
plt.xlabel("Stage duration (ms)")
plt.tight_layout(pad=0.2)
plt.savefig("figures/eeg_raw.pdf")
plt.show()
