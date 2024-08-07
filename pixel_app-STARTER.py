
from tkinter import *

root = Tk()
root.title ('Pixel Art')
root.geometry('500x500')

X_PIX, Y_PIX = 10, 10 # the grid will be 10 pixels wide, and 10 high

PIX_SIZE = int(400/X_PIX) # using 400 here so there is extra space in the window
'''
Global variables will be very important here!
Global variables are often written in all capital letters so they
are not mixed up with other variables.
Here, COLOUR refers to the currently selected colour for filling in the grid
'''

COLOUR = 'BLACK' # starting with BLACK because that is the colour of our background
c = Canvas(root, width=400, height=400, bg=COLOUR)
c.pack()


class Pixel():
    def __init__(self, x0, y0):
        self.fill= COLOUR
        self.outline_colour= 'white'

        x1,y1 = x0 + PIX_SIZE, y0 + PIX_SIZE
        # Now x0, y0, x1, y1 are the coordinates of the rectangle area of the screen where the pixel is placed
        self.obj = c.create_rectangle(x1,y1,x0,y0,fill=self.fill,outline='white')

    def colour_pixel(event):
        # Change the color of the selected pixel
        chosen_pixel = c.find_closest(event.x, event.y)[0]
        c.itemconfig(chosen_pixel, fill=COLOUR)
        # If grid lines are off, update the outline to match the fill color
        if not LINES_ON:
            c.itemconfigure(chosen_pixel, outline=COLOUR)



    def change_outline(self):
        '''
        This function is called on EACH pixel when the 'Outline?' button is
        pressed. It will switch the current outline of a pixel according to LINES_ON
    '''
        if LINES_ON:
             c.itemconfig(self.obj, outline='white')
        else:
             clr = c.itemcget(self.obj, 'fill')
             c.itemconfig(self.obj, outline=clr)

class ColourButton():
     def __init__(self, parent, colour):
          '''
          This is the function called when creating a ColourButton.
          TODO:
          - fill in the line indicated below.
          '''
          self.colour = colour
          self.Button = Button(parent, bg=colour, command=self.update)

     
     def update(self):
          '''
          This is the method that is the command for a ColourButton.

          When a ColourButton is pressed, it must ONLY change the global COLOUR
          variable to be this ColourButton's colour attribute/
          TODO:
          - fill in this function. It should be 2 lines.
          '''
          global COLOUR
          COLOUR = self.colour
          
def grid():
    global PIXEL_GRID
    for row in range(Y_PIX):
        for col in range(X_PIX):
            PIXEL_GRID[row][col] = Pixel(col * PIX_SIZE, row * PIX_SIZE)


def toggle_lines():
    global LINES_ON
    LINES_ON = not LINES_ON
    for row in PIXEL_GRID:
        for p in row:
            p.change_outline(LINES_ON)

############### MAIN CODE ###############


PIXEL_GRID = [[0 for i in range(X_PIX)] for j in range(Y_PIX)]
for row in range(Y_PIX):
        for col in range(X_PIX):
            PIXEL_GRID[row][col] = Pixel(row*PIX_SIZE, col * PIX_SIZE)
# PIXEL_GRID is a global variable that will be updated so it always reflects the current state of the grid

'''
TODO:
- Create a Frame to hold all your colour buttons called 'colour_bar'
- pack this frame into the window

- create a list of all the colours you will be making buttons for - as Strings called 'colours'
'''

menu_bar = Frame(root)
menu_bar.pack(fill=X)

colour_bar = Frame(root)
colour_bar.pack(side=TOP, fill=X)

# This loops over the list, creating and placing colour buttons
colours = ['red','blue','green','yellow','purple','pink','orange','black','white','grey']
for i in range(len(colours)):
    x = ColourButton(colour_bar, colours[i])
    x.Button.grid(row=0, column=i)

# LINES_ON represents whether the grid lines are showing right now
LINES_ON = True
# The button to control the outline is made and placed below
line_toggle = Button(colour_bar, text='Outline?', bg='black',fg='white', command=toggle_lines)
line_toggle.grid(row=0, column=i + 1)


'''
TODO:
- create your canvas, name it 'c'
- call the draw_grid function

- pack the canvas to the screen

- bind the action of filling in a pixel to mouse movement with the button down
- bind the q key to quitting

- call the mainloop method!
'''



grid()
c.bind("<B1-Motion>", Pixel.colour_pixel)

# Start the main loop
root.mainloop()