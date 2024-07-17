

from tkinter import *


def print_loc(event):
    print(event.x, event.y)


root = Tk()
w = 600
h = 600
c = Canvas(root, height=600, width=600, bg='yellow')
# frame
c.create_rectangle(50, 50, 600 - 50, 600 - 50,
                   fill="light blue", tags=('frame'))

# cat
c.create_polygon(210, 285, 175, 200, 260, 225, fill='brown', outline='black', tags=('ears'))
c.create_polygon(390, 285, 425, 200, 340, 225, fill='brown', outline='black', tags=('ears'))
c.create_polygon(225, 265, 210, 285, 175, 200, fill='white', outline='black', tags=('ears'))
c.create_polygon(390, 285, 375, 268, 424, 203, fill='white', outline='black', tags=('ears'))
c.create_oval(200, 200, 400, 400, fill="brown", tags=('head'))
c.create_oval(245, 280, 295, 330, fill='white', tags=('eyes'))
c.create_oval(355, 280, 305, 330, fill='white', tags=('eyes'))
c.create_oval(260, 300, 290, 330, fill='black', tags=('eyes'))
c.create_oval(340, 300, 310, 330, fill='black', tags=('eyes'))
c.create_oval(288, 330, 311, 351, fill='pink', tags=('nose'))
c.create_polygon(300, 360, 320, 370, 280, 330, tags=( 'mouth'))


c.pack()

def open_mouth():
    if c.itemcget(left_eye_pupil_1, 'state') == NORMAL:
        c.itemconfigure(left_eye_pupil_1, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_1, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_2, state=NORMAL)
        c.itemconfigure(right_eye_pupil_2, state=NORMAL)

def toggle_eyes():
    '''
    If using a global variable, include lines like this to 
    use and check that variable

    global crossed
    if not crossed:
    '''
    # This function uses the approach of checking an object's state to determine what version is currently used
    if c.itemcget(left_eye_pupil_1, 'state') == NORMAL:
        c.itemconfigure(left_eye_pupil_1, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_1, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_2, state=NORMAL)
        c.itemconfigure(right_eye_pupil_2, state=NORMAL)
        '''crossed = True # this is ESSENTIAL if using the global variable approach'''

    else:
        c.itemconfigure(left_eye_pupil_2, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_2, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_1, state=NORMAL)
        c.itemconfigure(right_eye_pupil_1, state=NORMAL)
        '''crossed = False'''

    # after 1000 milliseconds, call this function again
    root.after(1000, toggle_eyes)
left_eye_white = c.create_oval(355, 280, 305, 330, fill='white', tags=('eye'))
right_eye_white = c.create_oval(245, 280, 295, 330, fill='white', tags=('eye'))

# Normal pupils - the tags  here haven't been used in this example but they may be helpful for other events
left_eye_pupil_1 = c.create_oval(260, 300, 290, 330, fill='black', tags=(
    'eye', 'pupil', 'uncrossed'), state=HIDDEN)
right_eye_pupil_1 = c.create_oval(340, 300, 310, 330, fill='black', tags=(
    'eye', 'pupil', 'uncrossed'), state=HIDDEN)

# Crossed eye pupils
left_eye_pupil_2 = c.create_oval(247, 287, 277, 317, fill='black', tags=(
    'eye', 'pupil', 'crossed'), state=NORMAL)
right_eye_pupil_2 = c.create_oval(350, 290, 320, 320, fill='black', tags=(
    'eye', 'pupil', 'crossed'), state=NORMAL)

#opened mouth
#
# wow= c.create_oval(325, 350, 275, 370, fill= 'black', tags=('mouth'))

toggle_eyes()

root.bind("<Button-1>", print_loc)
root.mainloop()
