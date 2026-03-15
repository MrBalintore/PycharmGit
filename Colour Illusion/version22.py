import numpy as np
import matplotlib.pyplot as plt

# triangle side length
s = 4

# circle radius
r = 2

# equilateral triangle centers
A = (0, 0)
B = (s, 0)
C = (s/2, np.sqrt(3)/2 * s)

centers = [A, B, C]

fig, ax = plt.subplots()

# draw circles
for cx, cy in centers:
    circle = plt.Circle((cx, cy), r, fill=False, linewidth=2)
    ax.add_patch(circle)

# plot triangle points
x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]
ax.plot(x, y, linestyle="--")

# formatting
ax.set_aspect('equal')
ax.set_xlim(-3, s+3)
ax.set_ylim(-3, s+3)
ax.set_title("Three circles at equilateral triangle corners")

plt.show()
