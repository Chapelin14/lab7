import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
x,y,dy=np.loadtxt("Shema.txt", delimiter=' ', unpack=True)
an_x,an_y,an_dy=np.loadtxt("Resh.txt", delimiter=' ', unpack=True)

def f(y,x):
    y1,y2=y
    return [y2,-1.25*y2-0.5*y1+0.25*x*np.exp(-x)]

w=odeint(f,[1,0],x)
y1=w[:,0]
y2=w[:,1]
plt.figure()
plt.plot(x,y,label='y')
plt.plot(x,dy,label="y'")
plt.title("Приближенное решение")
plt.legend()
plt.figure()
plt.plot(y,dy)
plt.title("Фазовая траектория")
plt.xlabel('y')
plt.ylabel("y'")
plt.figure()
plt.plot(x,y-an_y)
plt.title("Разностный график для y (прибл) и y (точн)")
plt.figure()
plt.plot(x,dy-an_dy)
plt.title("Разностный график для y' (прибл) и y' (точн)")
plt.figure()
plt.plot(x,y,label='y приближенное')
plt.plot(x,y1,label='y (решение scipy)')
plt.legend()
plt.figure()
plt.plot(x,y-y1)
plt.title("Разностный график для y (прибл) и y (решение scipy)")
plt.figure()
plt.plot(x,dy-y2)
plt.title("Разностный график для y' (прибл) и y' (решение scipy)")



plt.show()
