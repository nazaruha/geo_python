import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

alph = 2.5
beta = 1.5
C = 0.02
B = 0.01
N = 100.
M = 100.


def Derivative(X, alph, beta, C):
    x, y = X
    dotX = x * (alph - C * y)
    dotY = y * (-beta + B * x)
    return np.array([dotX, dotY])


Nt = 1000
tMax = 30.
t = np.linspace(0., tMax, Nt)
X0 = [N, M]
res = integrate.odeint(Derivative, X0, t, args=(alph, beta, C, B))
x = res.T
y = res.T

plt.figure()
plt.grid()
plt.title('Графічне зображення отриманих даних')
plt.plot(t, x, 'xb', label='Жертва')
plt.plot(t, y, '+r', label='Хижак')
plt.xlabel('Час t, [дні]')
plt.ylabel('Популяція')
plt.legend()

plt.show()
