from uib_inf100_graphics.event_app import run_app
from uib_inf100_graphics.helpers import text_in_box

# Run this file to see how differt options affect strings drawn with
# the text_in_box -method.

def app_started(app):
    app.text = 'Hello World!'
    app.texts = [
        'Here is\na multi-line text!', 
        '      Spaces first, newline last\n',
        '1',
        '' # empty string
    ]

    app.font = None
    app.fonts = [
        # Named fonts (guaranteed to exist, but may differ between OS'es)
        'TkFixedFont',
        'TkDefaultFont', # None and not found fonts resolves to this

        # Very common system fonts (available on vast majority of systems)
        'Times new roman',
        'Arial',
        'Arial 20 overstrike', # Use tuple or string to specify options
        ('Arial', 20, 'bold'), # font size is ignored, but is still required
        ('Arial', 40, 'italic underline'),

        # Common system fonts (may not available on all systems, e.g. Linux)
        'Comic Sans MS',
        'Impact',

        # OS specific system fonts (probably not available on another OS)
        'Apple Chancery', # macOS only
        'Segoe Script', # Windows only
    ]
    app.fit_mode = 'contain'
    app.fit_modes = ['fill', 'width', 'height']

    app.justify = 'center'
    app.align = 'center'
    app.padding = 0
    app.min_font_size = 1
    app.fill = None
    app.fills = [ 'red', 'white', 'black', 'magenta', 'lightGreen', '#00308f' ]

def key_pressed(app, event):
    # Justify
    if event.key == "Left":
        app.justify = 'left' if app.justify == 'center' else 'center'
    elif event.key == "Right":
        app.justify = 'right' if app.justify == 'center' else 'center'
    # Align
    elif event.key == "Up":
        app.align = 'top' if app.align == 'center' else 'center'
    elif event.key == "Down":
        app.align = 'bottom' if app.align == 'center' else 'center'
    # Padding
    elif event.key == "p":
        app.padding = (app.padding + 10) % 50
    # Text
    elif event.key == "t":
        app.texts.append(app.text)
        app.text = app.texts.pop(0)
    # Fit mode
    elif event.key == "m":
        app.fit_modes.append(app.fit_mode)
        app.fit_mode = app.fit_modes.pop(0)
    # Font
    elif event.key == "f":
        app.fonts.append(app.font)
        app.font = app.fonts.pop(0)
    # Min font size
    elif event.key == "s":
        app.min_font_size = max(1, (app.min_font_size * 2) % 256)
    # Fill color
    elif event.key == "c":
        app.fills.append(app.fill)
        app.fill = app.fills.pop(0)

def draw_instructions(app, canvas, x1, y1, x2, y2):
    function_call = f"""\
text_in_box(canvas, {x1!r}, {y1!r}, {x2!r}, {y2!r},
        text={app.text!r},
        font={app.font!r},
        fit_mode={app.fit_mode!r},
        padding={app.padding!r},
        min_font_size={app.min_font_size!r},
        justify={app.justify!r},
        align={app.align!r},
        fill={app.fill!r}
)
"""
    canvas.create_text(10, 10, text=function_call, anchor='nw', font="TkFixedFont")

    # Instructions
    instructions = 'Press keys to change:\n'
    instructions += '  text -> t    \n'
    instructions += '  font -> f    \n'
    instructions += '  fit_mode -> m    \n'
    instructions += '  padding -> p    \n'
    instructions += '  min_font_size -> s    \n'
    instructions += '  justify -> Left/Right    \n'
    instructions += '  align -> Up/Down    \n'
    instructions += '  fill -> c    '
    canvas.create_text(app.width - 10, 10, text=instructions, anchor='ne', justify='right')
    canvas.create_text(app.width/2, app.height - 10, anchor='s',
                       text='Resize window to change bounding box. ' + 
                       f'Current size: {x2-x1}x{y2-y1}')
    
def redraw_all(app, canvas):
    x1, y1, x2, y2 = 50, 180, app.width-50, app.height-50
    draw_instructions(app, canvas, x1, y1, x2, y2)
    canvas.create_rectangle(x1, y1, x2, y2)
    text_in_box(canvas, x1, y1, x2, y2, text=app.text,
            font=app.font,
            fit_mode=app.fit_mode,
            padding=app.padding,
            min_font_size=app.min_font_size,
            justify=app.justify,
            align=app.align,
            fill=app.fill
    )

run_app(width=600, height=400, title='Text in box')