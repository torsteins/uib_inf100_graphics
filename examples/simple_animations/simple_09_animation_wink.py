from uib_inf100_graphics.simple import canvas, display

while True:
    # Normal face
    canvas.create_oval(10, 10, 390, 390, fill='yellow')
    canvas.create_oval(100, 100, 150, 150, fill='black')
    canvas.create_oval(250, 100, 300, 150, fill='black')
    canvas.create_arc(100, 100, 300, 320, start=200,
                      extent=140, width=5, style='chord')
    display(canvas, 4.8)

    # Winking face
    canvas.create_oval(10, 10, 390, 390, fill='yellow')
    canvas.create_oval(100, 100, 150, 150, fill='black')
    canvas.create_line(250, 125, 300, 125, width=5)
    canvas.create_arc(100, 100, 300, 320, start=200,
                      extent=140, width=5, style='chord')
    display(canvas, 0.2)

