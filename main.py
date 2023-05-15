import numpy as np
import matplotlib.pyplot as plt

def prelu_derivative(x, alpha=0.1):
    dx = np.ones_like(x)
    dx[x < 0] = alpha
    return dx

x = np.linspace(-8, 8, 100)
y = prelu_derivative(x)

fig, ax = plt.subplots()
ax.plot(x, y, color='blue')
ax.axhline(y=0, color='black', linestyle='solid')
ax.axvline(x=0, color='black', linestyle='solid')
ax.set_xlabel('x')
ax.set_ylabel('derivative of prelu')
ax.legend()
plt.show()
2