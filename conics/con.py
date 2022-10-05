import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt

mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color',['k'])
x = np.linspace(-9,9,400)
y = np.linspace(-5,5,400)
x,y = np.meshgrid(x,y)
def axes():
    plt.axhline(0,alpha=.1)
    plt.axvline(0,alpha=.1)
a = .3
axes()
plt.contour(x,y,(y**2-4*a*x),[0],colors = 'k')
#if using termux
plt.savefig('/sdcard/Download/FWC/trunk/conic_assignment/fig.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/FWC/trunk/conic_assignment/fig.pdf'")) 
