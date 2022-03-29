#!/usr/bin/env python3

from utils import save_pickle, read_pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import random

cmaps = {}

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

plt.figure(figsize=(5, 1))

ax = plt.gca()
plt.imshow(gradient, aspect='auto', cmap=plt.get_cmap("viridis"))
plt.text(
    0.035, -1, "0s",
    va='center',
    ha='right', fontsize=10,
    transform=ax.transAxes,
)
plt.text(
    1, -1, "44s",
    va='center',
    ha='right', fontsize=10,
    transform=ax.transAxes,
)

ax.set_axis_off()
plt.tight_layout(pad=0.1)
plt.savefig(
    "figures/et_sequence_cmap.png",
    dpi=250,
)
plt.show()