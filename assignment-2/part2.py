#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import residue

# Making the time axis
sampleFreq = 5000
tStep = 1 / sampleFreq
tLen  = 2
t = np.arange(0, tLen, tStep)

### -- Rectangular pulse
pLen = 10e-3   # Pulse length
amp  = 1       # Amplitude
cen  = 1       # Center of pulse

# Finding indices for start and stop
pStart = (cen - pLen/2) * sampleFreq
pStop  = (cen + pLen/2) * sampleFreq

# Producing the rectangular pulse
rectPulse = np.zeros(t.size)
rectPulse[pStart:pStop] = 1

plt.plot(t, rectPulse)
plt.xlim(0.9, 1.1)
plt.show()

### -- Triangular pulse

# Reusing the rect pulse attributes:
# pLen = 10e-3   # Pulse length
# amp  = 1       # Amplitude
# cen  = 1       # Center of pulse
# pStart = (cen - pLen/2) * sampleFreq
# pStop  = (cen + pLen/2) * sampleFreq 
pMid = cen * sampleFreq

# Producing the triangular pulse
triPulse              = np.zeros(t.size)
triPulse[pStart:pMid] = np.linspace(0, amp, (pMid-pStart))
triPulse[pMid:pStop]  = np.linspace(amp, 0, (pStop-pMid))

plt.plot(t, triPulse)
plt.xlim(0.9, 1.1)
plt.show()

### -- Gaussian pulse

# New attributes:
amp   = 7
pLen  = 3 * 10e-3
pSamp = pLen * sampleFreq
pInt  = slice(pMid - pSamp/2, pMid + pSamp/2)

gaussPulse = np.zeros(t.size)
x = np.linspace(0, pLen, pSamp)
gaussPulse[pInt] = np.exp(-((x - pLen/2)/(2 * pLen**2))**2)

plt.plot(t, gaussPulse)
plt.xlim(0.9, 1.1)
plt.show()

### -- Pulse train

numPulses = 11
tStart    = 1
period    = 10e-3
pWidth    = 1e-3

# To be used in for loop; has to be int
width  = int(pWidth * sampleFreq)
start  = int(tStart * sampleFreq)
period = int(period * sampleFreq)

pulseTrain = np.zeros(t.size)

for s in range(start, start + period*numPulses, period):
    pulseTrain[s:s+width] = 1

plt.plot(t, pulseTrain)
plt.xlim(1, 1.1)
plt.show()

