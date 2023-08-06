from uib_inf100_graphics.simple import canvas, display

# Arcs are drawn with the create_arc method. The arguments are the same as for
# create_oval and create_rectangle, and the arguments are describing the
# rectangular bounding box of the oval. The start and extent arguments are
# used to specify the start and end angles of the arc. The angles are measured
# in degrees, and the start angle is measured from the 3 o'clock position.
# Note that the angle is only correct if the width and height of the bounding
# box are equal, otherwise the figure will be stretched.

canvas.create_arc(10, 20, 390, 90, start=0, extent=270)
canvas.create_arc(10, 110, 390, 190, start=45, extent=270, fill='lightGreen')

# The style of the arc can be changed with the style argument. The style can
# be set to ARC, CHORD or PIESLICE. The default style is PIESLICE.

canvas.create_arc(50, 210, 390, 290, start=45, extent=270, style='chord',
                  fill='#eeaabb', outline="red", width=8)
canvas.create_arc(10, 310, 390, 390, start=45, extent=270, style='arc')


display(canvas)
