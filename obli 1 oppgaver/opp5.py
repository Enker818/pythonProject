from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("300x300")
root.title('Kalko')


a = 5
b = 9
c = 2.5
d = 21
e = 0


box = Label(root,text="Person 1: 5 småkaker\n"
                      "Person 2: 9 småkaker\n "
                      "Person 3: 2.5 småkaker\n "
                      "Person 4: 21 småkaker\n "
                      "Person 5: 0 småkaker\n ")
box.grid(row=0, column=0, columnspan=2, padx=5, pady=5,sticky='w')

output = Entry(root)


def svar1():
    output.delete(0, 'end')
    output.insert("end",int(a + b + c + d + e / 5))
def svar2():
    output.delete(0, 'end')
    output.insert("end",float(a + b + c + d + e / 5))


button_1 = Button(root, text="Svar på Int",
                      width=9, height=2,
                      bg="white", fg="black",command=svar1)
button_2 = Button(root, text="Svar på Float",
                      width=9, height=2,
                      bg="white", fg="black",command=svar2)


output.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')
button_1.grid(row=2, column=0, padx=(5, 0), pady=5, sticky='w')
button_2.grid(row=2, column=1, padx=(0, 5), pady=5, sticky='w')

root.mainloop()
