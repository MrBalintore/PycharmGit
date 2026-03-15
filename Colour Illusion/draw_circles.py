import svgwrite

# canvas size
width = 900
height = 700

# create SVG
dwg = svgwrite.Drawing("color_illusion.svg", size=(width, height))

# colors (approx extracted RGB)
blue_stripe = "rgb(5,10,196)"
white = "rgb(251,252,253)"
cyan = "rgb(15,247,253)"
magenta = "rgb(242,9,251)"
black = "rgb(2,0,7)"
dark_blue = "rgb(2,0,252)"

# circle positions
r = 180
top = (450, 260)
left = (310, 430)
right = (590, 430)

# draw circles
dwg.add(dwg.circle(center=top, r=r, fill=cyan))
dwg.add(dwg.circle(center=left, r=r, fill=magenta))
dwg.add(dwg.circle(center=right, r=r, fill=black))

# draw overlap tint (approximate central overlap)
dwg.add(
    dwg.circle(
        center=(450, 380),
        r=140,
        fill=dark_blue,
        opacity=0.9
    )
)

# vertical stripe overlay
stripe_width = 10

for x in range(0, width, stripe_width * 2):
    dwg.add(
        dwg.rect(
            insert=(x, 0),
            size=(stripe_width, height),
            fill=blue_stripe
        )
    )

dwg.save()
print("SVG saved as color_illusion.svg")
