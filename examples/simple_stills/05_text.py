from uib_inf100_graphics.simple import canvas, display

# Text is drawn with the create_text method. The first two arguments are the x
# and y coordinates of the anchor point of the text. To illustrate where the
# anchor point is, we draw a small pink circle at the anchor point in some of
# the examples below.

ax, ay = 200, 50
canvas.create_oval(ax - 5, ay - 5, ax + 5, ay + 5, fill='pink', outline='')
canvas.create_text(ax, ay, text='Hello, world!')


# The anchor argument can be used to change the anchor point of the text. The
# anchor point is the point on the text that is placed at the given x and y
# coordinates. The default anchor point is CENTER, which means that the center
# of the text is placed at the given coordinates. The anchor point can be
# changed to one of the following values:
# CENTER, N, NE, E, SE, S, SW, W, NW

ax, ay = 200, 100
canvas.create_oval(ax - 5, ay - 5, ax + 5, ay + 5, fill='pink', outline='')
canvas.create_text(ax, ay, text='Carpe diem!', anchor='sw')

ax, ay = 200, 150
canvas.create_oval(ax - 5, ay - 5, ax + 5, ay + 5, fill='pink', outline='')
canvas.create_text(ax, ay, text='Ay caramba!', anchor='n')

# The font argument can be used to change the font of the text. The font
# argument is a string that describes the font. The string consists of three
# parts: the font family, the font size, and the font style. The font family
# can be one of the following values: Arial, Courier, Helvetica, Times, or
# Symbol. The font size is a number that describes the size of the font. The
# font style can be one of the following values: normal, bold, italic, or
# bold italic. The font family and font style are optional, and the default
# values are Arial and normal.

ax, ay = 200, 200
canvas.create_text(ax, ay, text="Don't panic!", font='Times 20 italic bold')

ax, ay = 200, 250
canvas.create_text(ax, ay, text='Bazinga!', font='Courier 30 italic')

# The fill argument can be used to change the color of the text.
# The angle argument can be used to change the angle of the text. The angle
# argument is the angle in degrees that the text is rotated clockwise around
# the anchor point. The default value is 0.

ax, ay = 200, 300
canvas.create_oval(ax - 5, ay - 5, ax + 5, ay + 5, fill='pink', outline='')
canvas.create_text(ax, ay, text='I have a cunning plan!', fill='blue', anchor='w',
                   angle=-30)

# Multiple lines of text can be drawn by using the newline character (\n) in
# the text string. The justify argument can be used to change the
# justification of the text. The justify argument can be one of the following
# values: left, center, or right. The default value is left.

ax, ay = 200, 350
canvas.create_oval(ax - 5, ay - 5, ax + 5, ay + 5, fill='pink', outline='')
canvas.create_text(ax, ay, text='Here it is,\nyour moment of zen', anchor='ne',
                   justify='right')

display(canvas)
