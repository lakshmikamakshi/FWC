
#Code by GVV Sharma (works on termux)
#Feb 11, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the point on the x axis which is equidistant from 
#two given points

#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/download/10/codes/CoordGeo')        #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if


#Intersection of two lines
def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))

  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  print(p)
  P=LA.inv(N)@p.T
  P=P.reshape(2,1)
  print(P)
  return P
#Given points
O = np.array(([13,0]))
p = np.array(([0,0])).reshape(2,1)
r = 5
V = np.array([[1,0],[0,1]])
V1 = np.matrix(V)
u = np.array(([-13,0])).reshape(2,1)
f = 144

'''
lamda , P =LA.eigh(V)
if(lamda[1]==0):
        lamda = np.flip(lamda)
        P=np.flip(P,axis=1)
'''
sigma = (V@p+u)@(V@p+u).T - (p.T@V@p + 2*u.T@p + f)*V
s_l, s_v = LA.eigh(sigma)
n1 = s_v@np.array([np.sqrt(np.abs(s_l[0])), np.sqrt(np.abs(s_l[1]))])
n1 = n1.reshape(2,1)
n2 = s_v@np.array([np.sqrt(np.abs(s_l[0])), -np.sqrt(np.abs(s_l[1]))])

n2 = n2.reshape(2,1)
#m_coeff = [25,288,25]
#m = np.roots(m_coeff)
#print(m)
'''
eta = u@P[:,0]
a = np.vstack((u.T+eta*P[:,0].T,V))
b= np.hstack((-f,eta*P[:,0]-u))

c = 0.5*(LA.norm(u)**2-lamda[1]*f)/(u.T@n)
F = (c*n-u)/lamda[1]
fl = LA.norm(F)
m1 = np.array(([1,m[0]]))
m2 = np.array(([1,m[1]]))
#print((A.T@V@A + 2*u.T@A + f)*(m2.T@V@m2))
#print((m2.T@(V@A+u))**2-(A.T@V@A + 2*u.T@A + f)*(m2.T@V@m2))
d = np.sqrt((m2.T@(V@A+u))**2 - (A.T@V@A + 2*u.T@A + f)*(m2.T@V@m2))
print(d)
#d2 = np.sqrt((m2.T@(V@A+u))**2 - (A.T@V@A + 2*u.T@A + A)*(m2.T@V@m2))
k2 = (d-m2.T@(V@A+u))/(m2.T@V@m2)
k4 = (-d-m2.T@(V@A+u))/(m2.T@V@m2)
k3 = (-d-m1.T@(V@A+u))/(m1.T@V@m1)
k1 = (d-m1.T@(V@A+u))/(m1.T@V@m1)
#print(k1,k3,k2,k4)
'''
#A_ = np.LA.inv(V)
f0 = (u.T@V1.I@u)-f
k = np.sqrt(f0/(n1.T@V1.I@n1))
#print(k)
k = k.item(0)
E1 =  V.T@(-k*n1-u)
E2 = V.T@((k*n2)-u)
#G = np.array(([G[0],G[1]]))
##Generating all lines

E1= np.array(([E1.item(0),E1.item(1)])).reshape((2,1))
E2= np.array(([E2.item(0),E2.item(1)])).reshape((2,1))

x_AO = circ_gen(O,r)
x_AE1 = line_gen(p,E1)
x_AE2 = line_gen(p,E2)
plt.plot(x_AO[0,:],x_AO[1,:])
plt.plot(x_AE1[0,:],x_AE1[1,:])
#AE1 = A-E1
k = 0.7
B = k*E1
O=O.reshape(2,1)
#Reflection
m = B-O
n = omat@m
c = O.T@n
D = E1+2*(c-n.T@E1)/(LA.norm(n)**2)*n
#parameters for line AQ
##print(n1,n2)

#print(B.shape)
#Finding C
#parameters for line BD
m1 = B-D
n1 = omat@m1
#print(n1.shape,B.shape,n2.shape,p.shape)
#Intersection of BD and AQ
n1=n1.reshape(1,2)
n2=n2.reshape(1,2)
C = line_intersect(n1,B,n2,p)
##print(LA.norm(AE1))

x_BC = line_gen(B,C)
plt.plot(x_AE2[0,:],x_AE2[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
#Plotting all lines
#Labeling the coordinates
plt.scatter(E1[0],E1[1])
plt.scatter(E2[0],E2[1])
plt.scatter(O[0],O[1])
plt.scatter(p[0],p[1])
plt.scatter(B[0],B[1])
plt.scatter(D[0],D[1])
plt.scatter(C[0],C[1])
O = O.reshape(2,1)
p = p.reshape(2,1)
E1 =E1.reshape(2,1)
E2 =E2.reshape(2,1)
B =B.reshape(2,1)
C =C.reshape(2,1)
plt.annotate("O",(O[0],O[1]),textcoords="offset points",xytext=(0,10),ha='center')
plt.annotate("A",(p[0],p[1]),textcoords="offset points",xytext=(0,10),ha='center')
plt.annotate("B",(B[0],B[1]),textcoords="offset points",xytext=(0,10),ha='center')
plt.annotate("C",(C[0],C[1]),textcoords="offset points",xytext=(0,10),ha='center')
plt.annotate("P",(E1[0],E1[1]),textcoords="offset points",xytext=(0,10),ha='center')
plt.annotate("Q",(E2[0],E2[1]),textcoords="offset points",xytext=(0,10),ha='center')
plt.annotate("D",(D[0],D[1]),textcoords="offset points",xytext=(0,10),ha='center')
'''
tri_coords = np.vstack((p,O,E1,E2,B,C)).T
vert_labels = ['A','O','E1','E2','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[i,0, tri_coords[i,1]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

'''
'''
#plt.scatter(G1[0],G1[1])
'''
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/sdcard/download/FWC/trunk/fig.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/download/FWC/trunk/fig.pdf'")) 
#else
#plt.show()
