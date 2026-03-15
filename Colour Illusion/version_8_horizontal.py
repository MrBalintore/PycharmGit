import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from shapely.geometry import Point, box

# ----- geometry -----------------------------------------------------

r = 1.0
top = (r/2, np.sqrt(3)*r/2)
bl  = (0, 0)
br  = (r, 0)

C = Point(top).buffer(r, 256)   # cyan
M = Point(bl).buffer(r, 256)    # magenta
Y = Point(br).buffer(r, 256)    # yellow

regions = [
    (C.difference(M.union(Y)), "cyan"),
    (M.difference(C.union(Y)), "magenta"),
    (Y.difference(C.union(M)), "yellow"),
    (C.intersection(M).difference(Y), "blue"),
    (C.intersection(Y).difference(M), "green"),
    (M.intersection(Y).difference(C), "red"),
    (C.intersection(M).intersection(Y), "black"),
]

Y_only = Y.difference(C.union(M))

# ----- helper -------------------------------------------------------

def draw_geom(ax, geom, color):
    if geom.is_empty:
        return
    for g in getattr(geom, "geoms", [geom]):
        v = np.array(g.exterior.coords)
        codes = [Path.MOVETO] + [Path.LINETO]*(len(v)-2) + [Path.CLOSEPOLY]
        ax.add_patch(PathPatch(Path(v, codes), facecolor=color, edgecolor="none"))

# ----- plot ---------------------------------------------------------

fig, ax = plt.subplots()

for geom, col in regions:
    draw_geom(ax, geom, col)

xmin, xmax = -1.2, 2.2
ymin, ymax = -1.2, 2.2

stripe_w = 0.02
spacing  = 0.04

# horizontal blue stripes (black over yellow)
y = ymin
while y < ymax:
    stripe = box(xmin, y, xmax, y + stripe_w)
    draw_geom(ax, stripe.difference(Y), (0,0,1))
    draw_geom(ax, stripe.intersection(Y), "black")
    y += spacing

# horizontal white stripes between them (yellow-only)
y = ymin + spacing/2
while y < ymax:
    stripe = box(xmin, y, xmax, y + stripe_w)
    draw_geom(ax, stripe.intersection(Y_only), "white")
    y += spacing

ax.set_aspect("equal")
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.axis("off")

# ----- SVG output ---------------------------------------------------

plt.savefig("cmy_horizontal_stripe_circles.svg", format="svg", bbox_inches="tight")
plt.show()
