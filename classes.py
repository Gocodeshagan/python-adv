from tkinter import * 
root = Tk()
c = Canvas(root, height=600, width=600, bg='light blue')

class Fly():
    img = PhotoImage(file = 'flyguy.png')
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.obj = c.create_image(x,y,image= Fly.img)


    pass

class FlySwatter():
    pass

first_fly = Fly(100,100) # first_fly's x = 100, y = 100
second_fly = Fly(200,100) # this fly's x = 200, y = 100

a = Fly.img # by calling on the Class itself or…
b = first_fly.img # any instance of the class
print(a == b) # this is True, all flies use the same image
fx= first_fly.x # this gets the value 100 because of initialization on first line
sx = second_fly.x # this gets the value 200
second_fly.x = 50 # this changes the value! Remember these are just variables

c.pack()
root.mainloop()