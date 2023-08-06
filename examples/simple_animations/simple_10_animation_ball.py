from uib_inf100_graphics.simple import canvas, display, config

r = 15            # Radius
x, y = 200, 200   # Center of circle
dx, dy = 8, 5     # Speed

while True:
    # Move circle
    x += dx
    y += dy

    # Bounce off walls
    if x < r or x > config.width() - r:
        dx *= -1
    if y < r or y > config.height() - r:
        dy *= -1

    # Draw circle
    canvas.create_oval(x-r, y-r, x+r, y+r, fill='green')
    display(canvas)

