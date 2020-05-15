import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
data1=np.loadtxt("Shema.txt")
data2=np.loadtxt("Resh.txt")

def f(y,x):
    y1,y2=y
    return [y2,-1.25*y2-0.5*y1+0.25*x*np.exp(-x)]
x=np.linspace(0,2,200)
y0=[1,0]
w=odeint(f,y0,x)
y1=w[:,0]
y2=w[:,1]
fig=plt.figure(facecolor='white')
plt.plot(data1[:,0],data1[:,1],linewidth=2,label='y')
plt.plot(data2[:,0],data2[:,1],'--',linewidth=2,label='y(exact)')
plt.plot(data1[:,0],data1[:,2],linewidth=2,label="y'")
plt.legend()
plt.figure(2)
plt.plot(data1[:,1],data1[:,2])
plt.xlabel('y')
plt.ylabel("y'")
plt.figure(3)
plt.plot(data1[:,0],data1[:,1],linewidth=2,label='y(approximate solution)')
plt.plot(x,y1,'--',linewidth=2)

plt.show()
