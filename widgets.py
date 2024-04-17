from tkinter import *
root = Tk()

f = Frame(root)

f1 = Frame(f, height=400, width = 400, bg= 'red')
f2 = Frame(f1, height=200, width=200, bg= 'yellow')
f2.pack()
f1.pack()
f.pack()

img = PhotoImage(file='flyguy.png')
l1 = Label(f, image=img)
l1.pack()

l2 = Label(f,text='colours!', bg='black',fg='white', justify='center')
l2.pack()

b = Button(root, text='click here')
b.pack()
b['bg'] = 'blue'

def print_hello():

    print('hello')
b1 = Button(f,text='submit',command=print_hello, fg='black',state='normal')
b1.pack()


release = StringVar()

cb= Checkbutton(f,text='yes',variable=release)
cb.pack()



ra = Radiobutton(root,text='A', variable=release,value=0)
rb = Radiobutton(root,text='B', variable=release,value=1)
rp = Radiobutton(root,text='C', variable=release,value=2)
ra.pack()
rb.pack()
rp.pack()

textbox = StringVar()
entrybox = Entry(root,show = '*',textvariable=textbox)
entrybox.pack()

l2 = Label(f, text='colours!', bg='black', justify='center')
val = l2.cget('bg')
print(val) 
val = b1.cget('state')

l2.configure(text='new text', bg='blue')


root.mainloop()