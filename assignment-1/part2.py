#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lti, step, impulse, lsim, freqresp

def heav(x):
    if x == 0:
        return 0.5
    return 0 if x < 0 else 1

m = 1
b = 10
k = 50

num = [b, k]
den = [m, b, k]

sys = lti(num, den)

t, i = impulse(sys)
t, s = step(sys)

# -- Plot of impulse response

plt.plot(t, i, t, s)
plt.title('Impulse and Unit Step Response')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.xlim(xmax = max(t))
plt.legend(('Impulse Response', 'Unit Step Response'), loc = 0)
plt.grid()
plt.show()

# -- Plot of frequency response

w, H = freqresp(sys)

plt.figure()
plt.plot(w, H)
plt.title('Frequency response')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Gain')
plt.legend(('Frequency response'), loc = 0)
plt.grid()
plt.show()

T = np.linspace(-5, 25, 1000)
x1 = np.zeros(len(T))
x2 = np.zeros(len(T))
x3 = np.zeros(len(T))

omega = (2 * np.pi) / 10

for j in range(len(T)):
    x1[j] = 0.25 * np.sin(omega * T[j]) * heav(T[j])
    x2[j] = 0.25 * (heav(T[j] - 10) - heav(T[j] - 20))
    x3[j] = 0.10 * (heav(T[j] - 10) - heav(T[j] - 10.1))

T, y1, x1out = lsim(sys, x1, T)
T, y2, x2out = lsim(sys, x2, T)
T, y3, x3out = lsim(sys, x3, T)

plt.figure()
plt.plot(T, y1, T, y2, T, y3)
plt.title('Handlebar position')
plt.xlabel('Time [s]')
plt.ylabel('Position [m]')
plt.legend(('x1', 'x2', 'x3'), loc = 0)
plt.grid()
plt.show()

#tvals, yout, xout = lsim((num, den), x1, T)
#
#plt.figure()
#plt.plot(T, yout, T, x1)
#plt.title('Input')
#plt.xlabel('Time [s]')
#plt.ylabel('Amp [m]')
#plt.legend('Input signal')
#plt.grid()
#plt.show()
