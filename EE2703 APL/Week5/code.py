from pylab import *
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
from scipy.optimize import curve_fit
import math
Nx = 50
Ny = 50
radius = 0.35
Niter = 3250

phi = np.zeros((Nx,Ny),float32)
x = linspace(-0.5,+0.5,Nx)
y = linspace(-0.5,+0.5,Ny)

Y, X = meshgrid(y, x)
ii = where(X*X + Y*Y <= radius**2)
phi[ii] = 1.0
plt.contourf(x,y,phi, cmap=cm.jet)
plt.show()
errors = []
iteration = []
for k in range(Niter):
    oldphi = phi.copy()
    phi[1:-1,1:-1] = 0.25*(phi[1:-1,0:-2]+phi[1:-1,2:]+phi[0:-2,1:-1]+phi[2:,1:-1])

    # Adding boundary conditions that dphi/dx = 0]
    phi[1:-1,0] = phi[1:-1,1]
    phi[1:-1,Nx-1] = phi[1:-1, Nx-2]
    phi[0, 1:-1] = phi[1, 1:-1]
    phi[Nx-1, 1:-1] = phi[Nx-2, 1:-1]
    
    # Updating phi
    phi[ii] = 1.0
    errors.append((abs(phi-oldphi)).max())
    iteration.append(k)
    
# plt.semilogy(iteration,errors)
# plt.show()

iteration = np.array(iteration)
plt.loglog(iteration, errors)
plt.show()

def exponential_func(iteration, a, b):
    return a*np.exp(b*iteration)

params, covariance = curve_fit(exponential_func, iteration, errors)
a, b = params
fit = a*np.exp(b*iteration)

params2, covariance2 = curve_fit(exponential_func, iteration[500:], errors[500:])
a, b = params2
fit_after_500 = a*np.exp(b*iteration[500:])

plt.plot(iteration, errors)
# plt.semilogy(iteration,errors)
# plt.semilogy(iteration[::50],fit[::50])
# plt.semilogy(iteration[500::50], fit_after_500[::50])
plt.show()

fig4=figure(4) # open a new figure
ax=p3.Axes3D(fig4) # Axes3D is the means to do a surface plot
title('The 3-D surface plot of the potential')
surf = ax.plot_surface(Y, X, phi.T, rstride=1, cstride=1, cmap=cm.jet)
plt.show()

