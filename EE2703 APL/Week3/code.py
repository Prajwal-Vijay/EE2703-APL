from pylab import *
import scipy.special as sp
import pandas as pd
import numpy as np
N=101 # no of data points
k=9 # no of sets of data with varying noise

df = pd.read_csv('fitting.dat', sep='\s+', header=None)

def g(t, A, B):
    return A*sp.jn(2,t) + B*t

t=linspace(0,10,N)

# Part 1 -
# data = g(t,1.05,-0.105)
# plot(t, data)
# xlabel(r'$t$',size=20)
# ylabel(r'$f(t)$',size=20)
# sigma=logspace(-1,-3,9)[0]
# errorbar(t[::5],df[1][::5], sigma, fmt='ro')
# show()

# Part 2 -
# data = g(t, 1.05, -0.105)
# J = sp.jn(2,df[0])
# M = c_[J ,df[0]]
# Y = np.matmul(M,np.array([1.05,-0.105]))
# plot(df[0], data, df[0], Y)
# show()

# Part 3 -
rows, cols = 21, 21  # Example dimensions
e = [[0 for _ in range(cols)] for _ in range(rows)]

a = linspace(0,2,21)
b = linspace(-0.2,0,21)
A, B = np.meshgrid(a, b)
e = 1/101*np.sum((df[1]-(A*sp.jn(2,t) + B*t))**2)

plt.contour(a,b,e)
plt.show()