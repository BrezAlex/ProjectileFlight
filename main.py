import matplotlib.pyplot as plt
import numpy as np

g = 9.81
v0 = 10
alpha = 45
x0 = 0
y0 = 0
t = 0
dt = 0.005

x = []
y = []
y_value = 0

while t <= 2:
    t += float(dt)
    x_value = v0 * np.cos(alpha) * t
    y_value = v0 * np.sin(alpha) * t - (g * t ** 2)/2
    x.append(x_value)
    y.append(y_value)
    print(x_value, y_value)

plt.plot(x, y)
plt.show()

