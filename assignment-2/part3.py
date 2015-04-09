#! /usr/bin/env python

# Loading modules
from __future__      import division
import numpy as np
from   scipy.signal  import residue
from matplotlib      import pyplot as plt 
#%matplotlib inline

global PI
PI = np.pi

# import sympy
# from   sympy.abc    import s, t
# from   sympy        import apart, exp
# from   sympy        import inverse_laplace_transform as ilt
# 
# Xs = (2*s + 1) / ((s + 2) * (s + 3))
# Ys = (5*s**2 - 3*s + 2) / ((s + 1) * (s**2 + 2*s + 7))
# Zs = (1 + exp(-3*s)) / (s * (2*s + 5))
# 
# print apart(Xs, s)
# print apart(Ys, s)
# print apart(Zs, Zs, s)
# 
# #print ilt(apart(Xs, s), s, t)
# #print ilt(apart(Ys, s), s, t)
# #print ilt(apart(Zs, s), s, t)
# 
# print ilt(Xs, s, t)

x_num = [2, 1]
x_den = [1, 5, 6]
y_num = [5, 3, 2]
y_den = [1, 3, 9, 7]
z_num = [1]
z_den = [2, 5, 0]

x_residues, x_poles, _ =  residue(x_num, x_den)
y_residues, y_poles, _ =  residue(y_num, y_den)
z_residues, z_poles, _ =  residue(z_num, z_den)


print "Residues X: ", x_residues
print "Poles X: "   , x_poles
print "Residues Y: ", y_residues
print "Poles Y: "   , y_poles
print "Residues Z: ", z_residues
print "Poles Z: "   , z_poles

tLen = 5
t = np.arange(-1, tLen, tStep)
x = np.zeros(t.size)
y = np.zeros(t.size)
z = np.zeros(t.size)

def heaviside(x):
    if x == 0:
        return 0.5 
    return 0 if x < 0 else 1

for i in range(t.size):
    x[i] = (5*np.exp(-t[i]) - 3*np.exp(-2*t[i])) * heaviside(t[i])
    y[i] = ((5/3)*np.exp(-t[i]) \
            + (10/3)*np.exp(-t[i])*np.cos(np.sqrt(6)*t[i]) \
            - (13/np.sqrt(6))*np.exp(-t[i])*np.sin(np.sqrt(6)*t[i])) \
            * heaviside(t[i])
    z[i] = (1/5) * ((1 - np.exp(-(5/2)*t[i]))*heaviside(t[i]) \
            + (1 - np.exp(-(5/2)*(t[i]-3)))*heaviside(t[i]-3))

plt.plot(t, x)
plt.grid()
plt.xlabel('$x(t)$')
plt.ylabel('Amplitude')

plt.figure()
plt.plot(t, y)
plt.grid()
plt.xlabel('$y(t)$')
plt.ylabel('Amplitde')

plt.figure()
plt.plot(t, z)
plt.grid()
plt.xlabel('$z(t)$')
plt.ylabel('Amplitde')
