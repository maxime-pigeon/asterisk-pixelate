##############################################################################
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
    ImageObject,
    fill,
    rect,
    font,
    text,
    image,
    BezierPath,
    drawPath,
    stroke,
    savedState,
    textSize,
)

import random
import os

newDrawing()

##############################################################################
# DRAWBOT EDITOR

# Set the square in which we draw the path
box = 20
# Set spacing between squares
# TODO: Not working, see radius
spacing = 1.2
# Set contrast (default = 3)
contrast = 3
# Set image path
img = "/Users/maximepigeon/Desktop/mona.jpg"
# Calculate image size
img_width, img_height = imageSize(img)
# Calculate new desired image width
img_new_width = width() * 0.5
scale_factor = img_new_width / img_width

# Move image to center of canvas
# TODO: Is not totally centered?
translate(width() / 2 - img_width / 2, height() / 2 - img_height / 2)
# Scale image to desired size
scale(scale_factor, center=(img_width / 2, img_height / 2))

# Define the asterisks we want to use
asterisks = "*⁂⁑⊛⩮✢✣✤✥✱✲✳✺✻✼✽❃❉❊❋※⁕⚹❀✾⚛☀"

# Fonction to convert asterisk string to path, and center in square
def asterisk_path(x, y, gray):
    with savedState():
        # Translate to pixel coordonates with box center as origin
        translate(x - box / 2, y - box / 2)
        # Convert text to Bezier path, randomize asterisk
        path = BezierPath()
        path.text(random.choice(asterisks), font="Everson Mono", fontSize=100)
        # Calculate the width and height of the path
        min_x, min_y, max_x, max_y = path.bounds()
        path_w = max_x - min_x
        path_h = max_y - min_y
        # Calculate a scale based on the given path bounds and the box
        s = min([box / float(path_w), box / float(path_h)])
        # Scale based on gray value
        scale(gray, center=(box / 2, box / 2))
        # Scale to fit in box
        scale(s)
        # Translate the negative offset; letter could have overshoot
        translate(-min_x, -min_y)
        # Draw the path
        drawPath(path)


# Loop over the image grid cells to get average color
for x in range(0, img_width, box):
    for y in range(0, img_height, box):
        color = imagePixelColor(img, (x, y))
        if color:
            r, g, b, a = color
            # Average gray value from RGB (default = R + G + B / 3)
            gray = 1 - ((r + g + b) / contrast)
            # Calculate radius based on gray value and spacing
            radius = box * gray / spacing

            # Draw asterisk
            asterisk_path(x, y, gray)

# TODO:
# - Replace bottom row with credits

##############################################################################
# SAVE WORK

endDrawing()

current_directory = os.getcwd()
saveImage(current_directory + "/" + "preview.pdf")

##############################################################################
