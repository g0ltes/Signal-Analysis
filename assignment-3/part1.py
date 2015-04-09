#! /usr/bin/env python
#
# Part 1 of assignment 3 in signal analysis.

from __future__     import division
import numpy    as np
from scipy.io       import wavfile
from matplotlib     import pyplot   as plt

sf, data = wavfile.read('fysikk.wav')
duration = data.size / sf

time = np.linspace(0, duration, data.size)

print "sample rate = %s, length = %s samples (%s seconds)" % \
      (sf, data.size, duration)

# Plotting signal as function of time
plt.plot(time, data)
plt.grid()
plt.show()

# Cutting off second half of data
data = data[0:(data.size/2)]
time = time[0:(time.size/2)]

plt.figure()
plt.plot(time, data)
plt.grid()
plt.show()

#from scipy.fftpack  import fft
## Useful data from 0:08 - 0:13
#N = (13-8) * sf
#T = 1.0 / sf
#useful = data[(8*sf):(13*sf)]
#spectrum = fft(useful)
#x_spect = np.linspace(0.0, 1.0/(2.0*T), N/2)
#
#plt.plot(x_spect, 2.0/N * np.abs(spectrum[0:N/2]))
#plt.grid()
#plt.show()
