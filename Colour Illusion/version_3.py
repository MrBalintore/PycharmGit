import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from shapely.geometry import Point, box

r = 1.0

# triangle centres
c1 = (0, 0)                     # cyan
c2 = (r, 0)                     # magenta
c3 = (r/2, np.sqrt(3)*r/2)      # yellow

cyan_circle = Point(c1).buffer(r, resolution=256)
magenta_circle = Point(c2).buffer(r, resolution=256)
yellow_circle = Point(c3).buffer(r, resolution=256)

# CMY regions
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

# draw CMY regions
for geom, color in regions:
    if not geom.is_empty:
        path = shapely_to_path(geom)
        ax.add_patch(PathPatch(path, facecolor=color, edgecolor="none"))

# ---- STRIPES ----

xmin, xmax = -1, 2
ymin, ymax = -1, 2

stripe_width = 0.08
spacing = 0.16

x = xmin
while x < xmax:
    stripe = box(x, ymin, x + stripe_width, ymax)

    # part inside yellow circle → black
    inside = stripe.intersection(yellow_circle)

    # part outside yellow circle → blue
    outside = stripe.difference(yellow_circle)

    if not outside.is_empty:
        path = shapely_to_path(outside)
        ax.add_patch(PathPatch(path, facecolor=(0,0,1), edgecolor="none"))

    if not inside.is_empty:
        path = shapely_to_path(inside)
        ax.add_patch(PathPatch(path, facecolor="black", edgecolor="none"))

    x += spacing

ax.set_aspect("equal")
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.axis("off")

plt.show()
