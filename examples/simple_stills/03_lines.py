from uib_inf100_graphics.simple import canvas, display

# Lines are drawn with the create_line method. The arguments are the x and y
# coordinates of the start and end points of the line.

canvas.create_line(10, 20, 390, 90)
canvas.create_line(10, 110, 390, 190, fill='blue', arrow='first')

# It is possible to draw multiple connected lines with a single create_line
# call by providing a list of coordinates. The coordinates are interpreted as
# pairs of x and y coordinates, and each pair is used to draw a line.

canvas.create_line([10, 210, 390, 290, 50, 290, 390, 210],
                   fill='red', width=5)

# It is also possible to draw multiple lines with a single create_line call by
# providing a list of coordinate pairs. Setting the smooth argument to True
# will make the lines look more like a curve.

points = [(10, 310), (390, 390), (50, 390), (390, 310)]
canvas.create_line(points, fill='green', width=5, smooth=True)

display(canvas)
