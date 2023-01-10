import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

def bpsk(x):
    return 0.5*sp.erfc(x/np.sqrt(2))

samples = 500000
N = np.random.normal(0, 1, samples)
X = np.random.choice([-1, 1],samples)
A_db = np.arange(0, 10+1)
theory= []
numerical = []
for i in A_db:
    A = 10**(0.1*i)
    est = (np.count_nonzero((X == 1) & (A*X + N < 0)) + np.count_nonzero((X == -1) & (A*X + N > 0)))/samples
    numerical.append(est)
    theory.append(bpsk(A))

plt.semilogy(A_db, numerical, '*')
plt.semilogy(A_db, theory)
plt.grid()
plt.xlabel("$A_{dB}$")
plt.ylabel("$P_e(A_{dB})$")
plt.legend(['Numerical', 'Theory'])

plt.savefig('../../figs/bpsk_pe_snr.pdf')
plt.savefig('../../figs/bpsk_pe_snr.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter3/bpsk_pe_snr.pdf"))
#else
plt.show() #opening the plot window
