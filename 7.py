import matplotlib.pyplot as plt
import numpy as np
import math

data1 = np.loadtxt("x.txt")
x=np.linspace(0,1,1999)


def TR(x):
    return (x + 3) * math.exp(-x) + ((6. * math.sqrt(7.) * math.sin(math.sqrt(7.) * x / 8.))/7. - 2. * math.cos(math.sqrt(7) * x / 8.)) / math.exp(x*5./8.)
def Dx(x):
    return (-7. * (x + 2) * math.exp(5. * x / 8.) + 2. * (-math.sqrt(7.) * math.sin(math.sqrt(7.) * x / 8.) + 7. * math.cos(math.sqrt(7.) * x / 8.) * math.exp(x)) * math.exp(-13. * x / 8.)) / 7.

YY = [TR(i) for i in x]
TRp=[Dx(i) for i in x]

plt.figure(figsize=(16, 9))
plt.title("Решение", fontsize=14)
plt.plot(x,data1[:,0],label = 'Неявный метод для y')
plt.plot(x,YY,label='Точное решение для y')



plt.legend()
plt.ylabel('y')
plt.xlabel('x')
plt.minorticks_on()
plt.grid(which="both")
plt.show()

plt.figure(figsize=(16, 9))
plt.title("Производная", fontsize=14)
plt.plot(x,data1[:,1],label = "Неявный метод для y' ")
plt.plot(x,TRp,label="Точное решение для y' ")

plt.legend()
plt.ylabel('dy/dx')
plt.xlabel('x')
plt.minorticks_on()
plt.grid(which="both")
plt.show()


plt.figure(figsize=(16, 9))
plt.title("Фазовый портрет", fontsize=14)
plt.plot(data1[:,0], data1[:,1])
plt.xlabel("$y(x)$", fontsize=14)
plt.ylabel("$y'(x)$", fontsize=14)
plt.minorticks_on()
plt.grid(which="both")
plt.show()
