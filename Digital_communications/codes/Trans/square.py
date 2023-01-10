#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if


max_range=50
max_lim=15.0
x = np.linspace(0,max_lim,max_range)    #points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
x1 = np.random.normal(0, 1, simlen)
x2 = np.random.normal(0, 1, simlen)
v = x1**2 + x2**2

for i in range(0,max_range):
	err_ind = np.nonzero(v < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
pdf = np.gradient(err, x, edge_order=2)

plt.plot(x.T,err)   #plotting the CDF
plt.grid()          #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.savefig('../../figs/chisq_cdf.pdf')
plt.savefig('../../figs/chisq_cdf.png')

plt.show()
plt.close()
	
plt.plot(x,pdf)             # plotting estimated PDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')

plt.savefig('../../figs/chisq_pdf.pdf')
plt.savefig('../../figs/chisq_pdf.png')

plt.show()


