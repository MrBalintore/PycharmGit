import svgutils.transform as sg

# input SVG files (top → bottom)
files = [
    "cmy_stripe_circles_blue.svg",
    "cmy_horizontal_stripe_circles.svg",
    "cmy_red_stripe_circles.svg",
    "cmy_green_stripe_circles.svg",
]

figures = []
heights = []

# load SVGs
for f in files:
    fig = sg.fromfile(f)
    root = fig.getroot()
    w, h = fig.get_size()
    figures.append((root, float(h.replace("px","").replace("pt",""))))
    heights.append(float(h.replace("px","").replace("pt","")))

width = 800  # output width (adjust if needed)
total_height = sum(heights)

# create final figure
canvas = sg.SVGFigure(str(width), str(total_height))

y_offset = 0
elements = []

for root, h in figures:
    root.moveto(0, y_offset)
    elements.append(root)
    y_offset += h

canvas.append(elements)
canvas.save("stacked.svg")
