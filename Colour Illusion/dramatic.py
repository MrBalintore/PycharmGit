
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from shapely.geometry import Point, box
from shapely.affinity import rotate

# ----- geometry -----------------------------------------------------

r = 1.0
top = (r/2, np.sqrt(3)*r/2)
bl  = (0, 0)
br  = (r, 0)

C = Point(top).buffer(r, 256)
M = Point(bl).buffer(r, 256)
Y = Point(br).buffer(r, 256)

regions = [
    (C.difference(M.union(Y)), "cyan"),
    (M.difference(C.union(Y)), "magenta"),
    (Y.difference(C.union(M)), "yellow"),
    (C.intersection(M).difference(Y), "blue"),
    (C.intersection(Y).difference(M), "green"),
    (M.intersection(Y).difference(C), "red"),
    (C.intersection(M).intersection(Y), "black"),
]

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

# draw base CMY regions
for geom, col in regions:
    draw_geom(ax, geom, col)

xmin, xmax = -2, 3
ymin, ymax = -2, 3

stripe_w = 0.02
spacing  = 0.06

# ----- halftone stripe layers --------------------------------------

screens = [
    (C, (0,1,1), 15),   # cyan screen
    (M, (1,0,1), 75),   # magenta screen
    (Y, (1,1,0), 0),    # yellow screen
]

for circle, color, angle in screens:

    x = xmin
    while x < xmax:

        stripe = box(x, ymin, x + stripe_w, ymax)

        # rotate stripe screen
        stripe = rotate(stripe, angle, origin=(0,0))

        draw_geom(ax, stripe.difference(circle), color)
        draw_geom(ax, stripe.intersection(circle), "black")

        x += spacing

# ----- formatting ---------------------------------------------------

ax.set_aspect("equal")
ax.set_xlim(-1.2, 2.2)
ax.set_ylim(-1.2, 2.2)
ax.axis("off")

plt.savefig("cmy_rotated_halftone.svg", format="svg", bbox_inches="tight")
plt.show()
