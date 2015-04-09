#! /usr/bin/env python

from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# -- Adjustable parameters
a   = 100     # seconds
b   = 1       # seconds
f   = 500     # sample frequency
itv = 1/f     # sample interval

# -- Initializing arrays
pad = 2
t1  = np.arange(-pad, a+pad, itv)
t2  = np.arange(-pad, b+pad, itv)
x1  = np.zeros(t1.size)
x2  = np.zeros(t2.size)

# Rect functions
x1[abs(t1-a/2)/a < 1/2] = 1/a
x2[abs(t2-b/2)/b < 1/2] = 1/b

# Doing the convolution. The result is scaled by the sample interval
conv = convolve(x1, x2, mode="full") * itv

conv_pad = 2*pad
conv_len = a + b + conv_pad
tconv    = np.linspace(-conv_pad, conv_len, len(conv))

plt.plot(t1, x1)
plt.plot(t2, x2)
plt.plot(tconv, conv)
plt.xlabel("Time (s)")
plt.legend(["$x_1$", "$x_2$", "Convolution"])
plt.show()

# Exp function
t3  = np.arange(0, 0.2, itv)
x3  = np.exp(-20*t3)

conv3  = convolve(x3, x3) * itv
tconv3 = np.arange(0, len(conv3)) * itv

plt.figure()
plt.plot(tconv3, conv3)
plt.xlabel("Time (s)")
plt.legend(["Convolution"])
plt.show()
