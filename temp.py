from tkinter import *

root = Tk()
root.geometry("1280x720")
root.title('bruh')
root.resizable(False, False)
root.configure(background='black')

# Load the background image
bg = PhotoImage(file="quest.png")


# Create frames for each page
Page1 = Frame(root, bg='black')
Page2 = Frame(root, bg='black')
Page3 = Frame(root, bg='black')
Page4 = Frame(root, bg='black')
Page5 = Frame(root, bg='black')

Page1.grid(row=0, column=0, sticky="nsew")
Page2.grid(row=0, column=0, sticky="nsew")
Page3.grid(row=0, column=0, sticky="nsew")
Page4.grid(row=0, column=0, sticky="nsew")
Page5.grid(row=0, column=0, sticky="nsew")

#questions

que1 = ["Let him die and you grow strength", "Help him and save him from the pain", "Watch him suffer cuz you enjoy it"]


# Page 1 content
label = Label(Page1,
              text="This test is about her teaching\nThere will be 5 questions about it\nDon't worry, you don't need to write anything\nJust select the options you think are correct",
              font=('arial', 12, 'bold'),
              padx=1,
              pady=1,
              background='black',
              fg='white')

Pg1 = Label(Page1,
            text="Kreia's Exam",
            font=('arial', 40, 'bold'),
            bg='black',
            fg='white',
            padx=480,
            pady=5,
            image=bg,
            compound='bottom')


# Page 2 content
Pg2 = Label(Page2,
            text="The answers you choose will represent which side of the Force you stand on.\nIt's like a spectrum. If you are extreme on either the dark or light side,\nIt will mean you failed,\nAnd there will be punishment for such failure.",
            font=('arial', 12, 'bold'),
            padx=300,
            pady=20,
            background='black',
            image=bg,
            compound='top',
            fg='white')
# Page 3

Pg3 = Label(Page3,
               text="You see a man in pain due to a deadly plague\nAnd hes is on verge of death but he has a chance to recover,\nYou have the ability to heal him but let him die would benefit you greatly\n what do you do?",
               font=('arial', 12, 'bold'),
               background='black',
               fg='white',
               image=bg,
               compound='top'

)

Pg3.pack(padx=20, pady=10)


button_command = lambda: Page2.tkraise()
button_command1 = lambda: Page3.tkraise()
def button_command2():
    Page4.tkraise()
button_command3 = lambda: Page5.tkraise()

page1_button = Button(Page1, text="Lets Go",
                      width=10,
                      height=1,
                      bg="white",
                      fg="black",
                      command=button_command)

# Pack content for Page 1
Pg1.pack(pady=(40, 20))  # Added padding to avoid overlap
label.pack(pady=(10, 30))  # Added padding to adjust spacing
page1_button.pack()


page2_button = Button(Page2, text="I Understand",
                      width=10,
                      height=1,
                      bg="white",
                      fg="black",
                      command=button_command1)

# Pack content for Page 2
Pg2.pack()
page2_button.pack()

# Page 3 content
x = IntVar()

def order():
    if(x.get()==0):
        print("well done")
        button_command2()
    elif(x.get()==1):
        print("very well")
        button_command2()
    elif(x.get()==2):
        print("apaty is death")
        button_command2()



for index in range(len(que1)):
    answers1 = Radiobutton(Page3,
                           text=que1[index],
                           bg='black',
                           fg='white',
                           padx = 1,
                           pady = 1,
                           variable=x,
                           value=index,
                           anchor=W,
                           width=50,
                           command=order,
                           )

    answers1.pack(anchor=W, padx=450, pady=5)
root.after(5000000, button_command2)

# Page 4 content

page4_button = Button(Page4, text="Next Page",
                      width=10,
                      height=1,
                      bg="white",
                      fg="black",
                      command=button_command3)
page4_button.pack(pady=(50, 20))

# Page 5 content
page5_button = Button(Page5, text="Next Page",
                      width=10,
                      height=1,
                      bg="white",
                      fg="black",
                      command=None)
page5_button.pack(pady=(50, 20))

# Raise the first page to the top
Page1.tkraise()

root.mainloop()
