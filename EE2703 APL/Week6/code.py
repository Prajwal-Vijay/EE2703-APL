from pylab import *
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
from scipy.optimize import curve_fit
import math
import scipy.signal as sp

# Fs = sp.lti([1,0.5],[1,1,2.5])
# Xs = sp.lti([1,0.5], [1,3.25,4.75,5.625,0])
# t, x = sp.impulse(Xs, None, linspace(0,50,51))
# plot(t,x)
# show()

# p1 = poly1d([1,0.1,2.2525])
# p2 = poly1d([1,2.25,0])
# p = polymul(p1,p2)
# Fs = sp.lti([1,0.05], p)
# t, x = sp.impulse(Fs, None, linspace(0,50,51))
# plot(t,x)
# show()

# for w in linspace(1.4,1.6,5):
#     H = sp.lti([1],[1,0,2.25])
#     t = linspace(0, 50, 101)
#     f_ = np.cos(1.5*t)*np.exp(-0.05*t)
#     t,y,svec = sp.lsim(H,f_,t)
#     plot(t,y)
#     show()

