#!/usr/bin/env python3

from utils import save_pickle, read_pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import random

data = read_pickle("computed/et_small.pkl")
SCALE_X = 15
SCALE_Y = 15
DIM_X = 2000
DIM_Y = 2000

COLORS = ["tab:blue", "tab:red", "tab:green", "tab:brown"]
ALPHAS = [0.8, 0.6, 0.4, 0.2]
LABELS_NODE = ["TP9", "AF7", "AF8", "TP10"]

data_annotator = data[99]
time_0 = data_annotator[0][0]
time_1 = data_annotator[-1][0]-time_0
print(time_1/1000)
exit()
# data[2]
# data[14]
# data[30]

# data[52]
# data[72]
# data[99]

et_img = np.zeros((DIM_Y//SCALE_Y+1, DIM_X//SCALE_X+1))
for line_i, line in enumerate(data_annotator):
    x = line[1]
    y = line[2]
    if x >= DIM_X or y >= DIM_Y:
        continue
    x = (x+500) % DIM_X
    y = int(y/SCALE_Y)
    x = int(x/SCALE_X)
    et_img[y,x] = line_i/len(data_annotator)

plt.imshow(
    et_img,
    cmap="viridis",
    interpolation="lanczos",
)
plt.imsave(
    "figures/et_sequence_raw.png",
    et_img,
    cmap="viridis",
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
