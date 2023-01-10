import numpy as np
import matplotlib.pyplot as plt

max_lim = 20
max_pts = 70
x = np.linspace(-1, max_lim, max_pts) #points on x-axis
simlen = int(1e6) #number of samples
cdf = [] #declaring probability list
U_RV = np.loadtxt('uni.dat',dtype='double')
T_RV = -2*np.log(1-U_RV)

for i in range(0,max_pts):
	cdf_ind = np.nonzero(T_RV < x[i]) #checking probability condition
	cdf_n = np.size(cdf_ind) #computing the probability
	cdf.append(cdf_n/simlen) #storing the probability values in a list

def exp_cdf(x):
	return np.piecewise(x, [x<0, x>=0], [0, lambda x: 1-np.exp(-x/2)])

pdf = np.gradient(cdf, x, edge_order=2)

plt.plot(x,pdf,'x')
plt.plot(x,pdf)
plt.grid()

plt.xlabel('$x_i$')
plt.ylabel('$f_X(x_i)$')
plt.legend(["Numerical","Theory"])
plt.savefig('../../figs/log_uni_pdf.pdf')
plt.savefig('../../figs/log_uni_pdf.png')
plt.show()
plt.close()

plt.plot(x, cdf, 'x') #plotting CDF numerical
plt.plot(x, exp_cdf(x)) #plottong CDF theory
plt.grid()
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../../figs/log_uni_cdf.pdf')
plt.savefig('../../figs/log_uni_cdf.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter2/log_uni_cdf.pdf"))
#else
plt.show()
