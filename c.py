'''

Functional interactive calculator app.

'''
"""
TODO:
SETUP
1. Draw out your calculator on paper - think about what buttons should be included and how to arrange them
    MUST INCLUDE: 0,1,2,3,4,5,6,7,8,9,+,-,*,/, CLEAR, =
    OPTIONAL: any buttons you choose, like on OFF button linked to root.quit()
2. From this drawing determine what row and column each button should be placed in
3. Pick out a colour-scheme so that your design is attractive

CODING
1. Create a Label that uses the 'expression' StringVar as its textvariable
2. Customize the CalcButton class so that creating your Buttons is easy and standardized
    2.1 Add more parameters to the __init__ function so your buttons can be created inside it
    2.2 Set the 'command' for your Buttons to be 'self.onClick' so that you can use the premade functions
3. Create a Label that uses the 'expression' StringVar as its textvariable - this is the top of the calculator where the expression appears
4. Create your Buttons using the CalcButton class. Some buttons you may want to create without it, especially if they have special commands.
    4.1 Your '=' button, for example, should have its command set to the 'evaluate' function instead
    4.2 Your 'CLEAR' button should have its command set to the 'clear' function

"""

from tkinter import *
root = Tk()
root.title('Calculator')
root.geometry('200x250')
expression = StringVar()

class CalcButton():
    def __init__(self, frame, char, bgcol, fgcol, row, col, command=None):

        # Store button parameters as instance variables
        self.char = char

        # If command is not provided, use self.onClick as the default command
        if command == None:
            command = self.onClick

        # Create a Button widget and store it as 'obj' instance variable
        self.obj = Button(frame, text=char, command=command, bg=bgcol, fg=fgcol, relief='raised')
        self.obj.grid(row=row, column=col, sticky='news')

    def onClick(self):
        # When a button is clicked, add its character to the expression
        expression.set(expression.get() + self.char)

def clear():
    # Clear the expression
    expression.set('')

def delete():
    # Remove the last character from the expression
    expression.set(expression.get()[:-1])

def evaluate():
    try:
        # Evaluate the expression using the 'eval' function and update the result
        result = str(eval(expression.get()))
        expression.set(result)
    except Exception:
        # Handle any evaluation errors by displaying "Error"
        expression.set('Error')

# Create frames for the calculator components
mainframe = Frame(root, bg='light grey', padx=10, pady=15)
mainframe.grid(row=0, column=0, columnspan=4, rowspan=4, sticky='news')

exp_box = Label(mainframe, bg='white', fg='black', textvariable=expression,
                justify='right', relief='sunken', width=mainframe.winfo_width())
exp_box.grid(row=0, column=0, columnspan=5, sticky='news')

special_BFrame = Frame(mainframe, bg='light grey', relief='flat', padx=5, pady=5)
special_BFrame.grid(row=1, column=0, columnspan=4, sticky='ew')

numpad_frame = Frame(mainframe, bg='light grey', padx=5, pady=5, relief='flat')
numpad_frame.grid(row=2, column=0, rowspan=4, columnspan=4, sticky='news')

# Create calculator buttons
CalcButton(numpad_frame, '7', 'dark orange', 'white', 0, 0)
CalcButton(numpad_frame, '8', 'dark orange', 'white', 0, 1)
CalcButton(numpad_frame, '9', 'dark orange', 'white', 0, 2)
CalcButton(numpad_frame, '4', 'dark orange', 'white', 1, 0)
CalcButton(numpad_frame, '5', 'dark orange', 'white', 1, 1)
CalcButton(numpad_frame, '6', 'dark orange', 'white', 1, 2)
CalcButton(numpad_frame, '3', 'dark orange', 'white', 2, 0)
CalcButton(numpad_frame, '2', 'dark orange', 'white', 2, 1)
CalcButton(numpad_frame, '1', 'dark orange', 'white', 2, 2)
CalcButton(numpad_frame, '0', 'dark orange', 'white', 3, 0)

CalcButton(numpad_frame, '.', 'red', 'white', 3, 1)
CalcButton(numpad_frame, '=', 'red', 'white', 3, 2, command=evaluate)
CalcButton(numpad_frame, '/', 'red', 'white', 0, 3)
CalcButton(numpad_frame, '*', 'red', 'white', 1, 3)
CalcButton(numpad_frame, '-', 'red', 'white', 2, 3)
CalcButton(numpad_frame, '+', 'red', 'white', 3, 3)

CalcButton(special_BFrame, 'OFF', 'dark grey', 'black', 0, 0, command=root.quit)
CalcButton(special_BFrame, 'CLR', 'dark grey', 'black', 0, 1, command=clear)
CalcButton(special_BFrame, 'DEL', 'dark grey', 'black', 0, 2, command=delete)

# Configure rows and columns for proper resizing
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)

for i in range(3):
    mainframe.rowconfigure(i, weight=1)
    mainframe.columnconfigure(i, weight=1)

special_BFrame.rowconfigure(0, weight=0)
for i in range(3):
    special_BFrame.columnconfigure(i, weight=1)

for i in range(4):
    numpad_frame.rowconfigure(i, weight=1)
    numpad_frame.columnconfigure(i, weight=1)

# Start the main loop
root.mainloop()
