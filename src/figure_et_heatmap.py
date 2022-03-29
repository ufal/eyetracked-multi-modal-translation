#!/usr/bin/env python3

from utils import save_pickle, read_pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import random

data = read_pickle("computed/et_small.pkl")
SCALE_X = 15
SCALE_Y = 15
DIM_X = 1280
DIM_Y = 1024

COLORS = ["tab:blue", "tab:red", "tab:green", "tab:brown"]
ALPHAS = [0.8, 0.6, 0.4, 0.2]
LABELS_NODE = ["TP9", "AF7", "AF8", "TP10"]

print(len(data[0]))

et_img = np.zeros((DIM_Y//SCALE_Y+1, DIM_X//SCALE_X+1))

for data_annotator in data[:60]:
    for line in data_annotator:
        x = line[1]
        y = line[2]
        if x >= DIM_X or y >= DIM_Y:
            continue
        y = int(y/SCALE_Y)
        x = int(x/SCALE_X)
        et_img[y,x] += 1

plt.imshow(et_img, cmap="inferno", interpolation="lanczos")
plt.imsave(
    "figures/et_heatmap.png",
    et_img,
    cmap="inferno",
)
# bicubic, hermite, quadric
# 'antialiased', 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'blackman'
# plt.ylim(top=1250)
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.tight_layout(pad=0.2)
# plt.savefig("figures/et_sequence.pdf")
plt.show()
