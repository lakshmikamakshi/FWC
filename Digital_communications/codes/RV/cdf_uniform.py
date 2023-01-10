import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,40)   
simlen = int(1e6)          
err = []                   
randvar = np.loadtxt('uni.dat', dtype='double')

for i in range(0,40):
	err_ind = np.nonzero(randvar < x[i]) 
	err_n = np.size(err_ind) 
	err.append(err_n/simlen) 

plt.plot(x.T,err)   
plt.grid()          
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.savefig('../../figs/uni_cdf.pdf')
plt.savefig('../../figs/uni_cdf.png')

plt.show() 
