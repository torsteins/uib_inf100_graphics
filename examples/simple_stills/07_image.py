from uib_inf100_graphics.simple import canvas, display
from uib_inf100_graphics.helpers import load_image_http, scaled_image

# Load image using the load_image or load_image_http function.
image = load_image_http('https://tinyurl.com/inf100kitten-png')
canvas.create_image(180, 180, pil_image=image)
canvas.create_oval(180 - 3, 180 - 3, 180 + 3, 180 + 3, fill='red', outline='')

# The anchor argument specifies where the image should be placed
# relative to the coordinates. The default is 'center', but you can
# also use 'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw' to place the
# image relative to the given coordinates. In the examples here we
# show the anchor point with a small red circle.

# Adjust its image size with the scaled_image function.
smaller_image = scaled_image(image, 0.4)
canvas.create_image(250, 180, pil_image=smaller_image, anchor='nw')
canvas.create_oval(250 - 3, 180 - 3, 250 + 3, 180 + 3, fill='red', outline='')

display(canvas)

# Hint: When using images, keep in mind that loading an image from file
# or from the internet is a slow operation. Therefore, avoid loading
# the same image multiple times if at all possible. You should call the
# load_image(_http) function only once for each image and store the
# result in a variable. You can then use that variable as you want.

# Image credits: unsplash.com/@tranmautritam
