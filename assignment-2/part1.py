#! /usr/bin/env python

from __future__      import division
from numpy           import pi, sin, cos, sqrt, array, linspace, zeros
from scipy.integrate import odeint
from scipy.signal    import lti, lsim
from matplotlib      import pyplot as plt

R   = 15            # Resistance (ohms)
L   = 16e-3         # Inductance (henrys)
C   = 333e-6        # Capacitance (farads)
Q   = 0.66          # Initial charge stored in capacitor at t = 0
f   = 60            # Input voltage frequency
omg = 2*pi*f 
phi = 25*(pi/180)   # Phase of input voltage in radians
V0  = sqrt(2)*110   # Input voltage amplitude

# Defining the system in terms of its coefficients in Laplace space
num = [C, 0]
den = [L*C, R*C, 1]
sys = lti(num, den)

t = linspace(0, .1, 100)
u = V0 * sin(omg*t + phi)

# Calculating the current
T, i, _ = lsim(sys, u, t)

# Plots
plt.plot(T, i)
plt.xlim([0, .1])
plt.xlabel('Time $t$ (s)')
plt.ylabel('Current $I(t)$ (A)')
plt.grid()
plt.legend(['$I(t)$'])
plt.show()
