import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

#if using termux
#import subprocess
#import shlex
#end if

rng = np.random.default_rng()

A = 4
s0 = np.array([1,0]).reshape(2,1)
s1 = np.array([0,1]).reshape(2,1)
samples = 250
N = rng.normal(size=(2, samples))
s0_y = A*s0 + N
s1_y = A*s1 + N

# Condition is x^ = s0 if y>x, x^ = s1 if y<x
plt.scatter(s0_y[0], s0_y[1])
plt.scatter(s1_y[0], s1_y[1])
plt.plot(np.linspace(-1, A+1, 100), np.linspace(-1, A+1, 100), color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(["$y|s_0$","$y|s_1$"])
plt.grid()

plt.savefig('../../figs/biv_scatter.pdf')
plt.savefig('../../figs/biv_scatter.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/biv_scatter.pdf"))
#else
plt.show() #opening the plot window
