import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from shapely.geometry import Point
from shapely.ops import unary_union

r = 1.0

# Equilateral triangle centres
c1 = (0, 0)                       # cyan
c2 = (r, 0)                       # magenta
c3 = (r/2, np.sqrt(3)*r/2)        # yellow

# Create circle geometries
cyan_circle = Point(c1).buffer(r, resolution=256)
magenta_circle = Point(c2).buffer(r, resolution=256)
yellow_circle = Point(c3).buffer(r, resolution=256)

# Regions
c_only = cyan_circle.difference(magenta_circle.union(yellow_circle))
m_only = magenta_circle.difference(cyan_circle.union(yellow_circle))
y_only = yellow_circle.difference(cyan_circle.union(magenta_circle))

cm = cyan_circle.intersection(magenta_circle).difference(yellow_circle)
cy = cyan_circle.intersection(yellow_circle).difference(magenta_circle)
my = magenta_circle.intersection(yellow_circle).difference(cyan_circle)

cmy = cyan_circle.intersection(magenta_circle).intersection(yellow_circle)

regions = [
    (c_only, "cyan"),
    (m_only, "magenta"),
    (y_only, "yellow"),
    (cm, "blue"),
    (cy, "green"),
    (my, "red"),
    (cmy, "black")
]

def shapely_to_path(geom):
    vertices = []
    codes = []
    for polygon in getattr(geom, "geoms", [geom]):
        exterior = np.array(polygon.exterior.coords)
        vertices.extend(exterior)
        codes.extend([Path.MOVETO] + [Path.LINETO]*(len(exterior)-2) + [Path.CLOSEPOLY])
    return Path(vertices, codes)

fig, ax = plt.subplots()

for geom, color in regions:
    if not geom.is_empty:
        path = shapely_to_path(geom)
        patch = PathPatch(path, facecolor=color, edgecolor="none")
        ax.add_patch(patch)

ax.set_aspect("equal")
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.axis("off")

plt.show()
