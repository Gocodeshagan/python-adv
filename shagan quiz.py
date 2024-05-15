# '''
# Project Title:qiz
# Author:shagan
# Date:03021847

# [insert description of project and instructions for use]

# '''


# '''
# # TODO:
# - fill out titleblock
# - create at least 5 questions
#     - each question requires:
#         - it's own frame
#         - a label to ask the question (in this frame)
#         - a widget to get input (in this frame) ex. Button, Entry, RadioButton

# - each question must use a different type of widget for input - Get creative!
# - stylize the test to show off what you know! Use background and foreground
# colours, alignment settings, images, frame padding etc. to make it appealing

# '''


from tkinter import *
root = Tk()

f = Frame(root,width=600,height=400)
f.pack(expand=True)



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
v1 = StringVar()

f1 = Frame(f,padx=10,pady=10)
f1.pack()
l1 = Label(f1,text='Hollywood Movie Quiz', bg='blue',fg='white', justify='center')
l1.pack()
q1 = Label(f1,text='Who was the lead actor in the movie "The Wolf Of Wallstreet"?')
q1.pack()
a1 = Radiobutton(f1,text='Brad Pitt', variable=v1,value=0)
a2 = Radiobutton(f1,text='Joseph Stalin', variable=v1,value=1)
a3 = Radiobutton(f1,text='Leonardo DiCaprio', variable=v1,value=2)
a4 = Radiobutton(f1,text='Howie Mandel', variable=v1,value=3)
a1.pack()
a2.pack()
a3.pack()
a4.pack()

v2 = StringVar()
f2 = Frame(f,padx=10,pady=10)
f2.pack()
q2 = Label(f2,text='Which comedy movie involves two undercover cops infiltrating a highschool.')
q2.pack()
b1 = Radiobutton(f2,text='Pulp Fiction', variable=v2,value=0)
b2 = Radiobutton(f2,text='21 Jumpstreet', variable=v2,value=1)
b3 = Radiobutton(f2,text='Good cop Bad Cop', variable=v2,value=2)
b4 = Radiobutton(f2,text='Rush Hour', variable=v2,value=3)
b1.pack()
b2.pack()
b3.pack()
b4.pack()

v3 = StringVar()
f3 = Frame(f,padx=10,pady=10)
f3.pack()
q3 = Label(f3,text='What was the movie where the main character turns into a bat themed hero and starts to fight crime.')
q3.pack()
c1 = Radiobutton(f3,text='Spider-Man', variable=v3,value=0)
c2 = Radiobutton(f3,text='The Batman', variable=v3,value=1)
c3 = Radiobutton(f3,text='Morbius', variable=v3,value=2)
c4 = Radiobutton(f3,text='Barbie', variable=v3,value=3)
c1.pack()
c2.pack()
c3.pack()
c4.pack()

v4 = StringVar()
f4= Frame(f,padx=10,pady=10)
f4.pack()
q4 = Label(f4,text='Who is the main antagonist in the movie: "Pirates of the caribbean: Dead mans chest"')
q4.pack()
d1 = Radiobutton(f4,text='The Kraken', variable=v4,value=0)
d2 = Radiobutton(f4,text='Spongebob', variable=v4,value=1)
d3 = Radiobutton(f4,text='Adolf Hitler', variable=v4,value=2)
d4 = Radiobutton(f4,text='Davy Jones', variable=v4,value=3)
d1.pack()
d2.pack()
d3.pack()
d4.pack()

v5 = StringVar()
f5 = Frame(f,padx=10,pady=10)
f5.pack()
q5 = Label(f5,text='Who plays main character in "The Great Gatsby"?')
q5.pack()
d1 = Radiobutton(f5,text='Tom Holland',variable=v5,value=0)
d2 = Radiobutton(f5,text='Tony Ferguson',variable=v5,value=1)
d3 = Radiobutton(f5,text='Leonardo DiCaprio',variable=v5,value=2)
d4 = Radiobutton(f5,text='Tobey Macguire',variable=v5,value=3)

d1.pack()
d2.pack()
d3.pack()
d4.pack()

v6 = StringVar()
f6 = Frame(f,padx=10,pady=10)
f6.pack()
q6 = Label(f6,text='Whos story does the movie "Cinderella Man" tell?')
q6.pack()
d1 = Radiobutton(f6,text='Mike Tyson',variable=v6,value=0)
d2 = Radiobutton(f6,text='James Braddock',variable=v6,value=1)
d3 = Radiobutton(f6,text='Cinderella',variable=v6,value=2)
d4 = Radiobutton(f6,text='James Charles',variable=v6,value=3)

d1.pack()
d2.pack()
d3.pack()
d4.pack()

v7 = StringVar()
f7 = Frame(f,padx=10,pady=10)
f7.pack()
q7 = Label(f7,text='Which animated movie was the first movie to ever use ray-tracing technology?')
q7.pack()
d1 = Radiobutton(f7,text='Big Hero 6',variable=v7,value=0)
d2 = Radiobutton(f7,text='Spider-Man: Into the Spiderverse',variable=v7,value=1)
d3 = Radiobutton(f7,text='Cars',variable=v7,value=2)
d4 = Radiobutton(f7,text='Encanto',variable=v7,value=3)

d1.pack()
d2.pack()
d3.pack()
d4.pack()

v8 = StringVar()
f8 = Frame(f,padx=10,pady=10)
f8.pack()
q8 = Label(f7,text='Which is the highest grossing video game movie')
q8.pack()
d1 = Radiobutton(f8,text='The Angry Birds Movie',variable=v7,value=0)
d2 = Radiobutton(f8,text='Pixels',variable=v7,value=1)
d3 = Radiobutton(f8,text='Uncharted',variable=v7,value=2)
d4 = Radiobutton(f8,text='Warcraft',variable=v7,value=3)

d1.pack()
d2.pack()
d3.pack()
d4.pack()








# This submit button should be at the end of your test
# It is meant to be clicked once the user has answered all questions
# submitButton = Button(root, text='Submit Answers',
#                       bg='white', command=check_answers)
# submitButton.pack()

# # This results label will display the number of questions answered correctly
# # Feel free to change up the code for submitButton and results to make
# # the test prettier and individualized!
# results = Label(root, textvariable=result)
# results.pack()

root.mainloop()