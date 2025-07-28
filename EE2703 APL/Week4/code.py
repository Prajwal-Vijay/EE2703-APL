from pylab import *
import scipy.interpolate
import scipy.special as sp
import pandas as pd
import numpy as np
import math
import scipy.integrate

def exp(x):
    return np.exp(x)

def g(x):
    return np.cos(np.cos(x))

x=linspace(0,2*pi,401)
plt.semilogy(x, exp(x))
plt.show()

# plot(x, g(x))
# show()

def u(x, k):
    return exp(x)*np.cos(x*k)

def v(x, k):
    return exp(x)*np.sin(x*k)

x = linspace(-2*math.pi, 4*math.pi, 1000)
an_1 = []
k = 0
an_1.append(1/(2*math.pi)*scipy.integrate.quad(u, 0, 2*math.pi, args=(k,))[0])
for k in range(1,26):
    an_1.append(1/(math.pi)*scipy.integrate.quad(u, 0, 2*math.pi, args=(k,))[0])
bn_1 = []
for k in range(1,26):
    bn_1.append(1/math.pi*scipy.integrate.quad(v, 0, 2*math.pi, args=(k,))[0])

def u(x, k):
    return g(x)*np.cos(x*k)

def v(x, k):
    return g(x)*np.sin(x*k)

x = linspace(-2*math.pi, 4*math.pi, 1000)
an_2 = []
k = 0
an_2.append(1/(2*math.pi)*scipy.integrate.quad(u, 0, 2*math.pi, args=(k,))[0])
for k in range(1,26):
    an_2.append(1/(math.pi)*scipy.integrate.quad(u, 0, 2*math.pi, args=(k,))[0])
bn_2 = []
for k in range(1,26):
    bn_2.append(1/math.pi*scipy.integrate.quad(v, 0, 2*math.pi, args=(k,))[0])
cn_2 = []
cn_2.append(an_2[0])
for i in range(1, 26):
    cn_2.append(an_2[i])
    cn_2.append(bn_2[i-1])

cn_2 = np.array(cn_2)
print(cn_2)

x=linspace(0,2*pi,401)
x=x[:-1] # drop last term to have a proper periodic integral
b=exp(x) # f has been written to take a vector
A=zeros((400,51)) # allocate space for A
A[:,0]=1 # col 1 is all ones
for k in range(1,26):
    A[:,2*k-1]=cos(k*x) # cos(kx) column
    A[:,2*k]=sin(k*x) # sin(kx) column

cn_1=lstsq(A,b)[0] # the ’[0]’ is to pull out the
# best fit vector. lstsq returns a list.

plt.plot(x,np.matmul(A,cn_1))
plt.show()