from pylab import plot, xlim, ylim, grid, show, rc, figure, xlabel, ylabel, linspace, math, legend
from scipy.integrate import odeint
import numpy as np

filename = "x.txt"
x_mod, dx_mod = np.loadtxt(filename, delimiter=' ', unpack=True)
t = linspace(0, 2, 200)
def func(y, t):
    x, v = y
    return [v, (t*math.exp(-t)-5*v-2*x)/4]

result = odeint(func, [1, 0], t)
x = result[:,0]
v = result[:,1]

### y(x)
figure(1)
plot(t,x,'r', label="График Scipy решения")
t=np.linspace(0,1,1999)
plot(t, x_mod, 'b', label="График исходного приближенного решения")
xlim(0, 1)
legend()
grid()
show()

### y'(x)
figure(2)
t = linspace(0, 2, 200)
plot(t, v, 'r', label="График производной Scipy решения")
t=np.linspace(0,1,1999)
plot(t, dx_mod, 'b', label="График производной исходного приближенного решения")
xlim(0, 1)
legend()
grid()
show()

### Фазовые траектории
figure(3)
t = linspace(0, 2, 200)
plot(x,v,'r', label="Фазовая диаграмма Scipy решения")
t=np.linspace(0,1,1999)
plot(x_mod, dx_mod, 'b', label="Фазовая диаграмма исходного приближенного решения")
xlabel("x")
ylabel("v")
legend()
xlim(0, 1.025)
grid()
show()

