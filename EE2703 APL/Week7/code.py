from sympy import *
import pylab as p

s = symbols('s')
def lowpass(R1,R2,C1,C2,G,Vi):
    A = Matrix([[0,0,1,-1/G],[-1/(1+s*R2*C2),1,0,0],
    [0,-G,G,1] , [-1/R1-1/R2-s*C1,1/R2,0,s*C1]])
    b = Matrix([0,0,0,Vi/R1])
    V = A.inv*b
    return (A,b,V)

A,b,V = lowpass(10000, 10000, 1e-9, 1e-9, 1.586, 1)
print('G=1000')
Vo=V[3]
print(Vo)
w=p.logspace(0,8,801)
ss=1j*w
hf=lambdify(s,Vo,'numpy')
v=hf(ss)
p.loglog(w,abs(v),lw=2)
p.grid(True)
p.show()