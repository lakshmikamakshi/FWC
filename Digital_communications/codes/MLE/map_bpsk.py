import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

def gauss_fun(x, mean, stdev):
    return np.exp(-(x-mean)**2/(2*stdev**2))/(stdev*np.sqrt(2*np.pi))

p = 0.3
A_db = 3
A = 10**(0.1*A_db)
d = np.log((1-p)/p)/(2*A)
x = np.linspace(-A-3, A+3, 100)
x0_y = p*gauss_fun(x, A, 1)
x1_y = (1-p)*gauss_fun(x, -A, 1)

plt.plot(x, x0_y)
plt.plot(x, x1_y)
plt.vlines(d, np.min(x1_y), np.max(x1_y), colors=['green'])
plt.grid()
plt.xlabel("$y$")
plt.ylabel("$P_X(x)P_Y(y|x)$")
plt.legend(['$pP_Y(y|x=1)$', '$(1-p)P_Y(y|x=-1)$', "$y=\\frac{1}{2A}\ln\left(\\frac{1}{p}-1\\right)$"])

plt.savefig('../../figs/bpsk_map_density.pdf')
plt.savefig('../../figs/bpsk_map_density.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/bpsk_map_density.pdf"))
#else
plt.show() #opening the plot window
