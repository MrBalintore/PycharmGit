import svgutils.transform as sg

files = [
    "cmy_stripe_circles_blue.svg",
    "cmy_horizontal_stripe_circles.svg",
    "cmy_red_stripe_circles.svg",
    "cmy_green_stripe_circles.svg",
]

# load figures
figs = [sg.fromfile(f) for f in files]
roots = [f.getroot() for f in figs]

# get size from first SVG
width, height = figs[0].get_size()
width = float(width.replace("px","").replace("pt",""))
height = float(height.replace("px","").replace("pt",""))

# create canvas for 2x2 grid
canvas = sg.SVGFigure(str(width*2), str(height*2))

# position each image
roots[0].moveto(0, 0)          # top-left
roots[1].moveto(width, 0)      # top-right
roots[2].moveto(0, height)     # bottom-left
roots[3].moveto(width, height) # bottom-right

canvas.append(roots)
canvas.save("cmy_stripe_grid.svg")
