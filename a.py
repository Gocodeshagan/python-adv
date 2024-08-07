from tkinter import *

# Create the main application window
root = Tk()
root.title('Pixel Art')
root.geometry('600x700')

# Variables
X_PIX = 20
Y_PIX = 20
PIX_SIZE = int(400 / X_PIX)
COLOUR = 'BLACK'
PIXEL_GRID = [[0 for _ in range(X_PIX)] for _ in range(Y_PIX)]
LINES_ON = True

# Class for handling individual pixels
class Pixel():
    def __init__(self, x1, y1):
        self.fill = COLOUR
        self.outline_colour = 'white'
        x2, y2 = x1 + PIX_SIZE, y1 + PIX_SIZE
        # Create a rectangle (pixel) on the canvas
        self.obj = c.create_rectangle(
            x1, y1, x2, y2, fill=self.fill, outline='white')

    def fill_colour(event):
        # Change the color of the selected pixel
        chosen_pixel = c.find_closest(event.x, event.y)[0]
        c.itemconfig(chosen_pixel, fill=COLOUR)
        # If grid lines are off, update the outline to match the fill color
        if not LINES_ON:
            c.itemconfigure(chosen_pixel, outline=COLOUR)

    def outline(self, show_lines):
        # Toggle the grid lines on/off for this pixel
        if show_lines:
            c.itemconfig(self.obj, outline='white')
        else:
            clr = c.itemcget(self.obj, 'fill')
            c.itemconfig(self.obj, outline=clr)

# Class for handling color buttons
class ColourButton():
    def __init__(self, parent, colour):
        self.colour = colour
        self.Button = Button(parent, bg=colour, command=self.update)

    def update(self):
        # Update the global color variable when a color button is clicked
        global COLOUR
        COLOUR = self.colour

# Function to draw the initial grid of pixels
def draw_grid():
    global PIXEL_GRID
    for row in range(Y_PIX):
        for col in range(X_PIX):
            PIXEL_GRID[row][col] = Pixel(col * PIX_SIZE, row * PIX_SIZE)

# Function to toggle grid lines on/off
def toggle_lines():
    global LINES_ON
    LINES_ON = not LINES_ON
    for row in PIXEL_GRID:
        for p in row:
            p.outline(LINES_ON)

# Function to clear all pixels
def clear_pixels():
    for row in PIXEL_GRID:
        for p in row:
            c.delete(p.obj)

# Menu bar frame
menu_bar = Frame(root)
menu_bar.pack(fill=X)

# Width and Height Entry
width_label = Label(menu_bar, text='Width:')
width_label.pack(side=LEFT)
width_entry = Entry(menu_bar)
width_entry.pack(side=LEFT)
width_entry.insert(0, str(X_PIX))

height_label = Label(menu_bar, text='Height:')
height_label.pack(side=LEFT)
height_entry = Entry(menu_bar)
height_entry.pack(side=LEFT)
height_entry.insert(0, str(Y_PIX))

def set_dimensions():
    # Set the new dimensions and redraw the grid
    global X_PIX, Y_PIX
    X_PIX = int(width_entry.get())
    Y_PIX = int(height_entry.get())
    clear_pixels()
    draw_grid()

set_dimensions_button = Button(menu_bar, text='Set Dimensions', command=set_dimensions)
set_dimensions_button.pack(side=LEFT)

# Title Entry
title_label = Label(menu_bar, text='Title:')
title_label.pack(side=LEFT)
title_entry = Entry(menu_bar)
title_entry.pack(side=LEFT)

def set_title():
    # Set the window title to the value entered in the title entry
    root.title(title_entry.get())

set_title_button = Button(menu_bar, text='Set Title', command=set_title)
set_title_button.pack(side=LEFT)

# Toggle Lines Button
toggle_lines_button = Button(menu_bar, text='Toggle Grid Lines', command=toggle_lines)
toggle_lines_button.pack(side=LEFT)

# Clear Button
clear_button = Button(menu_bar, text='Clear', command=clear_pixels)
clear_button.pack(side=LEFT)

# Color Buttons
colour_bar = Frame(root)
colour_bar.pack(side=TOP, fill=X)  # Use side=TOP to expand vertically

colours = ['red', 'orange', 'yellow', 'green', 'blue',
           'purple', 'black', 'white', 'magenta', 'cyan', 'brown']

for colour in colours:
    x = ColourButton(colour_bar, colour)
    x.Button.pack(side=LEFT)

# Canvas
c = Canvas(root, width=400, height=400, bg=COLOUR)
c.pack()
draw_grid()
c.bind("<B1-Motion>", Pixel.fill_colour)

# Start the main loop
root.mainloop()
