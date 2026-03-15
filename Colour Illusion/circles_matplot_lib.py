import numpy as np
import matplotlib.pyplot as plt

# canvas
width = 900
height = 700

img = np.ones((height, width, 3))

# colors (normalized 0–1)
cyan = np.array([15,247,253])/255
magenta = np.array([242,9,251])/255
black = np.array([2,0,7])/255
blue = np.array([5,10,196])/255
dark_blue = np.array([2,0,252])/255

# circle parameters
r = 180
top = (450,260)
left = (310,430)
right = (590,430)

Y, X = np.ogrid[:height, :width]

def draw_circle(center, radius, color):
    cx, cy = center
    mask = (X-cx)**2 + (Y-cy)**2 <= radius**2
    img[mask] = color

# draw circles
draw_circle(top, r, cyan)
draw_circle(left, r, magenta)
draw_circle(right, r, black)

# approximate overlap tint
draw_circle((450,380), 140, dark_blue)

# stripe overlay
stripe_width = 10

for x in range(0, width, stripe_width*2):
    img[:, x:x+stripe_width] = blue

# display
plt.figure(figsize=(8,6))
plt.imshow(img)
plt.axis('off')
plt.show()
