import matplotlib.pyplot as plt
import numpy as np

g = 9.81
v0 = 10
alpha = 45
x0 = 0
y0 = 0
t = 1
dt = input("Введите значение dt: ")

x = []
y = []

while y <= 0:



# vx = []
# vy = []
#
# while t <= 10:
#     t += float(dt)
#     vx_value = v0 * np.cos(alpha)
#     vy_value = v0 * np.sin(alpha) - g * t
#     vx.append(vx_value)
#     vy.append(vy_value)
#
# v = np.sqrt(vx_value ** 2 + vy_value ** 2)
# print(v)
# print(vx)
# print(vy)
#
# plt.plot(vx, vy)
# plt.show()