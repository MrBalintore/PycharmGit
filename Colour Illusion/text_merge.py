import os
files = [
    "cmy_stripe_circles_blue.svg",
    "cmy_horizontal_stripe_circles.svg",
    "cmy_red_stripe_circles.svg",
    "cmy_green_stripe_circles.svg",
]
command = f"type {" ".join(files)} > bigfile.txt"
print("command={command}")
os.system(command)
