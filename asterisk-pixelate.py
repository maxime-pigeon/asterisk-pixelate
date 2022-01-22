########################################################################
# SETTINGS

from drawBot import (
    newDrawing,
    imageSize,
    scale,
    width,
    height,
    endDrawing,
    saveImage,
    translate,
    imagePixelColor,
    oval,
    size,
)

import os

newDrawing()

########################################################################
# DRAWBOT EDITOR

size(700, 1000)

path = "/Users/maximepigeon/Desktop/screen.png"
img_width, img_height = imageSize(path)
img_new_width = width() * 0.75
scale_factor = img_new_width / img_width
grid_size = 20
spacing = 1.2

translate(width() / 2 - img_width / 2, height() / 2 - img_height / 2)

scale(scale_factor, center=(img_width / 2, img_height / 2))


# Loop over the image grid cells to get average color
for x in range(0, img_width, grid_size):
    for y in range(0, img_height, grid_size):
        color = imagePixelColor(path, (x, y))
        if color:
            r, g, b, a = color
            # Average gray value from RGB (default = R + G + B / 3)
            gray = 1 - ((r + g + b) / 4)
            # Calculate radius based on gray value and spacing
            radius = grid_size * gray / spacing
            # Draw oval
            oval(x - radius / 2, y - radius / 2, radius, radius)

# TODO:
# - Use asterisk shape instead of oval
# - Randomize which asterisk shapes is used
# - Replace bottom row with credits

########################################################################
# SAVING WORK

endDrawing()

current_directory = os.getcwd()
saveImage(current_directory + "/" + "preview.pdf")

########################################################################
