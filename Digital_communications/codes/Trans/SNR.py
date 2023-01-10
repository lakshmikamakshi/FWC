import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

rng = np.random.default_rng()

G_min = -5
G_max = 5
samples = 500000

bin_min= -6
bin_max= 6
num = 50
hist = np.linspace(bin_min,bin_max, num)
limit = np.where(hist > 0)[0][0]

numeric = []
theory = []
G_db = np.arange(G_min, G_max + 1)
for i in G_db:
    G = 10**(0.1*i)
    A_sam= rng.rayleigh((G/2)**0.5, samples) 
    N_sam = rng.normal(size=samples) 
    numeric.append(np.count_nonzero(A_sam+N_sam < 0)/samples)
    theory.append(0.5-0.5*np.sqrt(G)/np.sqrt(2+G))
plt.semilogy(G_db,numeric, 'X')
plt.semilogy(G_db,theory)
plt.grid()
plt.xlabel('$\gamma$')
plt.ylabel('$P_e(\gamma)$')
plt.legend(["Simulated","Theory"])

plt.savefig('../../figs/prob_error.pdf')
plt.savefig('../../figs/prob_error.png')
plt.show()


# Inference: Easier computation, switching of operations pe and convolution (instead of convolution, doing expected val)
