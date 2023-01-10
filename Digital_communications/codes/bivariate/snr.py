import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

#if using termux
#import subprocess
#import shlex
#end if

rng = np.random.default_rng()
samples = 500000

s0 = np.array([1,0]).reshape(2,1)
snr_max = 11
snr_db = np.arange(0, snr_max+1)

estimate = np.zeros(snr_db.shape[0])
theory = np.zeros(snr_db.shape[0])
for i in snr_db:
    N = rng.normal(size=(2, samples))
    snr = 10**(0.1*i)
    Y = snr*s0 + N
    est = np.count_nonzero(np.where(Y[0] < Y[1], 1, 0))/samples
    estimate[i] = est
    th = 0.5*sp.erfc(snr/2)
    theory[i] = th

plt.semilogy(snr_db, estimate, 'o')
plt.semilogy(snr_db, theory)
plt.grid()
plt.xlabel('$SNR_{dB}$')
plt.ylabel('$P_e(SNR_{dB})$')
plt.legend(["Numerical","Theory"])

plt.savefig('../../figs/biv_pe_vs_snr.pdf')
plt.savefig('../../figs/biv_pe_vs_snr.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/biv_pe_vs_snr.pdf"))
#else
plt.show() #opening the plot window
