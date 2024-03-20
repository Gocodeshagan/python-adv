from tkinter import *
import random
root = Tk()
c = Canvas(root, height=600, width=600, bg='light blue')
class Bug():

    def __init__(self, x, y, bug_image):
        self.x = x
        self.y = y
        self.obj = c.create_image(x,y, image = bug_image)
        c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)
        
    def destroy(self, event): # ignore the 'event' parameter, we will learn later
        c.delete(self.obj)
        print('Got one!')
        

class Fly(Bug): # Notice the Bug in brackets! Parent class goes between brackets
    img = PhotoImage(file = 'C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\\Shagan\\py adv 1\\flyguy.png')
    
    def __init__(self, x, y):
        super().__init__(x, y, Fly.img )
    

#     pass

# class LadyBug(Bug):
#     img = PhotoImage(file='small_ladybug.png')
#     def __init__(self, x, y):
#         super().__init__(x, y, LadyBug.img )
        
# class FlySwatter():
    # pass

first_fly = Fly(100,100) # first_fly's x = 100, y = 100
second_fly = Fly(200,100) # this fly's x = 200, y = 100

a = Fly.img # by calling on the Class itself or…
b = first_fly.img # any instance of the class
print(a == b) # this is True, all flies use the same image
fx= first_fly.x # this gets the value 100 because of initialization on first line
sx = second_fly.x # this gets the value 200
second_fly.x = 50 # this changes the value! Remember these are just variables

for i in range(10):
    Fly(random.randrange(0,400), random.randrange(0,400))
    # LadyBug(random.randrange(0,400), random.randrange(0,400))


c.pack()
root.mainloop()
