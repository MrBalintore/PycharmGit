import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# radius = side length
r = 1.0

# coordinates of equilateral triangle
x1, y1 = 0, 0
x2, y2 = r, 0
x3, y3 = r/2, np.sqrt(3)*r/2

fig, ax = plt.subplots()

# circles with multiply-style overlap
circles = [
    Circle((x1, y1), r, color='cyan', alpha=0.8),
    Circle((x2, y2), r, color='magenta', alpha=0.8),
    Circle((x3, y3), r, color='yellow', alpha=0.8)
]

for c in circles:
    ax.add_patch(c)

# formatting
ax.set_aspect('equal')
ax.set_xlim(-r, 2*r)
ax.set_ylim(-r, 2*r)
ax.axis('off')

plt.show()
