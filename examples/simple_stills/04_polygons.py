from uib_inf100_graphics.simple import canvas, display

# Polygons are drawn with the create_polygon method. The arguments are the x
# and y coordinates of the vertices of the polygon. The polygon is drawn with
# a black fill and no outline by default, but this can be changed with the
# outline and fill arguments. The width argument can be used to change the
# width of the outline. To set the fill to be transparent, use the empty
# string as the fill.

canvas.create_polygon(10, 20, 390, 90, 10, 90)
canvas.create_polygon(10, 110, 390, 190, 10, 190,
                      fill='', outline='red', width=3)

# It is also possible to provide a list of points to the create_polygon method.
# The points are interpreted as pairs of x and y coordinates.

points = [50, 210, 390, 290, 50, 290, 390, 210]
canvas.create_polygon(points, fill='lightGreen', outline='black', width=1)

# It is also possible to provide a list of coordinate pairs to the method.
# If smooth is set to True the polygon will look more like a curve.

points = [(10, 310), (390, 390), (50, 390), (390, 310)]
canvas.create_polygon(points, fill='darkblue', smooth=True)


display(canvas)
