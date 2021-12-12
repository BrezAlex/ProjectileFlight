import matplotlib.pyplot as plt
import numpy as np

g = 9.81
v0 = 10
alpha = 45
t = 0
dt = 0.005
m = 1
R = 1.4

x = []
y = []
x1 = []
y1 = []

while t <= 2: # без сопротивления
    t += dt
    x_value = v0 * np.cos(alpha) * t
    y_value = v0 * np.sin(alpha) * t - (g * t ** 2) / 2
    x.append(x_value)
    y.append(y_value)
    print(x_value, y_value)
    if y_value < 0:
        break

t = 0
while t <= 2:
    t += dt
    exp = np.exp(-R * t / m)
    x1_value = (v0 * np.cos(alpha) * m / R) * (1 -exp)
    y_one = (m * g + v0 * np.sin(alpha) * R) * m
    y1_value = (- (y_one * exp) / (R ** 2)) - (g * m * t / R) + y_one / R ** 2
    x1.append(x1_value)
    y1.append(y1_value)
    print(x1_value, y1_value)
    if y1_value < 0:
        break

plt.title('Траектории')
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, x1, y1)

plt.show()


