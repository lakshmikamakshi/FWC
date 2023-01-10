import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

samples = 250
X = np.random.binomial(1, 0.5, samples)*2-1
N = np.random.normal(0, 1,samples)
A_db = 5
A = 10**(0.1*A_db)
Y = A*X + N

x0 = np.extract(X==1, X)
x1 = np.extract(X==-1, X)
n0 = np.extract(X==1, N)
n1 = np.extract(X==-1, N)
y0 = A*x0 + n0
y1 = A*x1 + n1
plt.plot(np.zeros(y1.shape[0]), y1,'*', mfc='none')
plt.plot(np.zeros(y0.shape[0]), y0, '*', mfc='none')

plt.plot(np.linspace(-0.1,0.1,10) ,np.zeros(10), color="green")
plt.grid()
plt.legend(["$y|1$","$y|0$"])

plt.savefig('../../figs/bpsk_scatter.pdf')
plt.savefig('../../figs/bpsk_scatter.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter3/bpsk_scatter.pdf"))
#else
plt.show() #opening the plot window
