'''
Project Title:qiz
Author:shagan
Date:03021847

[insert description of project and instructions for use]

'''


'''
TODO:
- fill out titleblock
- create at least 5 questions
    - each question requires:
        - it's own frame
        - a label to ask the question (in this frame)
        - a widget to get input (in this frame) ex. Button, Entry, RadioButton

- each question must use a different type of widget for input - Get creative!
- stylize the test to show off what you know! Use background and foreground
colours, alignment settings, images, frame padding etc. to make it appealing

'''


from tkinter import *
root = Tk()

f = Frame(root)
f2 = Frame(f, height=50, width=600, bg= 'blue')
f2.pack()
f.pack()

# These lists will hold each of your StringVars (1 per question)
# and expected answers (1 per question)
# As you create your questions, append to these lists so that stringvars[i]
# is considered correct if it's value is equal to answers[i]
stringvars = []
answers = []

result = StringVar()


def check_answers():
    points = 0
    for i in range(len(answers)):
        if stringvars[i].get() == answers[i]:
            points += 1
    result.set(str(points))

# Add all your questions and widgets here
l1 = Label(f,text='Hollywood Movie Quiz', bg='blue',fg='white', justify='center')
q1 = Label(f,text='Who was the lead actor in the movie "The Wolf Of Wallstreet"?')
a1 = Radiobutton(root,text='Brad Pitt', variable=result,value=0)
a2 = Radiobutton(root,text='Joseph Stalin', variable=result,value=1)
a3 = Radiobutton(root,text='Leonardo DiCaprio', variable=result,value=2)
a4 = Radiobutton(root,text='Howie Mandel', variable=result,value=3)
a1.pack()
a2.pack()
a3.pack()
a4.pack()

q2 = Label(f,text='Which comedy movie involves two undercover cops infiltrating a highschool.')
b1 = Radiobutton(root,text='Pulp Fiction', variable=result,value=0)
b2 = Radiobutton(root,text='21 Jumpstreet', variable=result,value=1)
b3 = Radiobutton(root,text='Good cop Bad Cop', variable=result,value=2)
b4 = Radiobutton(root,text='Rush Hour', variable=result,value=3)
b1.pack()
b2.pack()
b3.pack()
b4.pack()

q3 = Label(f,text='What was the movie where the main character turns into a bat themed hero and starts to fight crime.')
c1 = Radiobutton(root,text='Spider-Man', variable=result,value=0)
c2 = Radiobutton(root,text='The Batman', variable=result,value=1)
c3 = Radiobutton(root,text='Morbius', variable=result,value=2)
c4 = Radiobutton(root,text='Barbie', variable=result,value=3)
c1.pack()
c2.pack()
c3.pack()
c4.pack()

q4 = Label(f,text='Who is the main antagonist in the movie: "Pirates of the caribbean: Dead mans chest"')
d1 = Radiobutton(root,text='The Kraken', variable=result,value=0)
d2 = Radiobutton(root,text='Spongebob', variable=result,value=1)
d3 = Radiobutton(root,text='Adolf Hitler', variable=result,value=2)
d4 = Radiobutton(root,text='Davy Jones', variable=result,value=3)
d1.pack()
d2.pack()
d3.pack()
d4.pack()

q1.pack()
q2.pack()
q3.pack()
l1.pack()




# This submit button should be at the end of your test
# It is meant to be clicked once the user has answered all questions
submitButton = Button(root, text='Submit Answers',
                      bg='white', command=check_answers)
submitButton.pack()

# This results label will display the number of questions answered correctly
# Feel free to change up the code for submitButton and results to make
# the test prettier and individualized!
results = Label(root, textvariable=result)
results.pack()

root.mainloop()
