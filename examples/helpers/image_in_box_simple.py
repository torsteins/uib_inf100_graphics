from uib_inf100_graphics.simple import canvas, display
from uib_inf100_graphics.helpers import load_image_http, image_in_box

# Use the image_in_box function to draw an image within a rectangle.

image = load_image_http('https://tinyurl.com/inf100kitten-png')

image_in_box(canvas, 20, 40, 180, 180, image)
canvas.create_rectangle(20, 40, 180, 180, outline='red', width=2)
canvas.create_text(100, 35, text="fit_mode='contain'", anchor='s')

# The image_in_box function can be configured to fit the image within the
# rectangle in different ways. The default is 'contain', which means that the
# image is scaled down to fit within the rectangle, but may leave empty space
# within the rectangle. The 'fill' mode scales the image to fill the
# rectangle, but may crop the image if the aspect ratio of the rectangle and
# the image are different. The 'stretch' mode scales the image to fill the
# rectangle, but may distort the image if the aspect ratio of the rectangle
# and the image are different. The 'crop' mode will not scale the image,
# but will crop the image to fit within the rectangle.

image_in_box(canvas, 20, 220, 180, 360, image, fit_mode='crop')
canvas.create_rectangle(20, 220, 180, 360, outline='red', width=2)
canvas.create_text(100, 215, text="fit_mode='crop'", anchor='s')

image_in_box(canvas, 220, 40, 380, 180, image, fit_mode='stretch')
canvas.create_rectangle(220, 40, 380, 180, outline='red', width=2)
canvas.create_text(300, 35, text="fit_mode='stretch'", anchor='s')

image_in_box(canvas, 220, 220, 380, 360, image, fit_mode='fill')
canvas.create_rectangle(220, 220, 380, 360, outline='red', width=2)
canvas.create_text(300, 215, text="fit_mode='fill'", anchor='s')

display(canvas)

# Image credits: unsplash.com/@tranmautritam
