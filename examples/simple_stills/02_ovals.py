from uib_inf100_graphics.simple import canvas, display

# Ovals are drawn with the create_oval method. The arguments are the same as
# for create_rectangle, and the arguments are describing the rectangular
# bounding box of the oval. Compare create_oval with create_rectangle with
# the same arguments:

canvas.create_oval(10, 20, 390, 90)
canvas.create_rectangle(10, 20, 390, 90)

canvas.create_oval(10, 110, 390, 190, fill='lightGreen')
canvas.create_oval(50, 210, 390, 290, fill='#eeaabb', outline="red", width=3)
canvas.create_oval(10, 310, 390, 390, fill='#00308f', width=0)

display(canvas)
