from tkinter import *
root = Tk()
root.title('Paint')
f=Frame(root)
f.pack()
COLOUR = 'black'
SIZE = 10

c = Canvas(root, bg='white', height=1000, width=1000)
c.pack()


class ColourButton():
    
     def __init__(self, colour):
          
          self.colour = colour
          self.Button = Button(f, bg=colour, command=self.update)
     
     def update(self):
          
          global COLOUR
          COLOUR = self.colour
          
     
def draw_circle(event):
     c.create_oval(event.x,event.y, event.x + SIZE.get(), event.y + SIZE.get(), fill=COLOUR, outline= COLOUR)
     c.pack()
    
def clear_canvas():
     c.delete(ALL)
     ''' '''
    

#################### MAIN CODE #########################


colours = ['red','blue','green','yellow','purple','pink','orange','black','white','grey']
for i in range(len(colours)):
    x = ColourButton(colours[i])
    x.Button.grid(row=0, column=i)

'''
Next create the CLEAR button and the width slider.

TODO:
- complete the code fragments below
'''
clear_button = Button(f, text='CLEAR', command= clear_canvas)
clear_button.grid(row = 0, column = i + 1)

SIZE = IntVar() # We are using the global variable as the int var so it is always updated
scalebar = Scale(f, variable = SIZE, bg = 'black', tickinterval=1,  resolution = 1, orient = HORIZONTAL, from_ = 1, to = 10)
scalebar.grid(row = 0, column = i + 2)

'''
TODO:
- bind the event of mouse button held down while moving ON THE CANVAS to the draw_circle function
- bind the letter q to quitting the program
- mainloop!
'''
c.bind("<B1-Motion>", draw_circle) 
root.bind("<q>", quit)
root.mainloop()
