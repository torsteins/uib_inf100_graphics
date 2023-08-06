from uib_inf100_graphics.simple import canvas, display

# Rectangles are drawn with the create_rectangle method. The arguments are
# describing the rectangular bounding box of the rectangle. The first two
# arguments are the x and y coordinates of the upper left corner, and the last
# two arguments are the x and y coordinates of the lower right corner. 

# The rectangle is drawn with a black outline and no fill by default, but this
# can be changed with the outline and fill arguments. The width argument can
# be used to change the width of the outline.

canvas.create_rectangle(10, 20, 390, 90)
canvas.create_rectangle(10, 110, 390, 190, fill='lightGreen')
canvas.create_rectangle(50, 210, 390, 290,
                        fill='#eeaabb', outline="red", width=3)
canvas.create_rectangle(10, 310, 390, 390, fill='#00308f', width=0)

display(canvas)
