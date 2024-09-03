from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("220x250")
root.title('Kalko')


a = 6
b = 3
c = 2

text = Label(root,text="trykk på sprøsmål får du svaret")
output = Entry(root)
def svar1():
    output.delete(0, 'end')
    output.insert("end",str(a + b * c ))
def svar2():
    output.delete(0, 'end')
    output.insert("end",str((a + b) * c ))
def svar3():
    output.delete(0, 'end')
    output.insert("end",str( a / b / c))
def svar4():
    output.delete(0, 'end')
    output.insert("end",str(a / (b / c)  ))

button_1 = Button(root, text="a)",
                      width=5, height=2,
                      bg="white", fg="black",command=svar1)
button_2 = Button(root, text="b)",
                      width=5, height=2,
                      bg="white", fg="black",command=svar2)
button_3 = Button(root, text="c)",
                      width=5, height=2,
                      bg="white", fg="black",command=svar3)
button_4 = Button(root, text="d)",
                      width=5, height=2,
                      bg="white", fg="black",command=svar4)
text.grid()
output.grid()
button_1.grid(row=3,column=0,sticky='w')
button_2.grid(row=4,column=0,sticky='w')
button_3.grid(row=5,column=0,sticky='w')
button_4.grid(row=6,column=0,sticky='w')
root.mainloop()
