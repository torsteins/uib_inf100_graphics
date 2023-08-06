from uib_inf100_graphics.simple import canvas, display
from uib_inf100_graphics.helpers import text_in_box

text = "Hello, world!"

# First example
canvas.create_rectangle(100, 20, 300, 70)
text_in_box(canvas, 100, 20, 300, 70, text)

# Named fonts and padding. A list of named fonts always available:
# https://tkinter-docs.readthedocs.io/en/latest/generic/fonts.html
# Depending on OS, there may be other named fonts available as well.
canvas.create_rectangle(100, 120, 300, 170)
text_in_box(canvas, 100, 120, 300, 170, text,
            font="TkFixedFont",
            padding=15)

# System installed font family name, fill color and vertical alignment.
canvas.create_rectangle(100, 200, 300, 270)
text_in_box(canvas, 100, 200, 300, 270, text,
            font="Times new roman",
            align='top',
            fill="blue")

# Multiline text, font style, justification.
multiline_text = text+"\n"+text+" "+text+"\n"+text
canvas.create_rectangle(100, 320, 300, 370)
text_in_box(canvas, 100, 320, 300, 370, multiline_text,
            font="Arial 42 bold italic overstrike underline",
            justify="right", # justify is 'left', 'center' or 'right'
            padding=5)

display(canvas)