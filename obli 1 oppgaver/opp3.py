from tkinter import *
import tkinter as tk



root = Tk()
root.geometry("220x400")
root.title('Kalko')

#operatorer
button_1 = Button(root, text="+",
                      width=2, height=2,
                      bg="white", fg="black",)
button_2 = Button(root, text="-",
                      width=2, height=2,
                      bg="white", fg="black",)
button_3 = Button(root, text="*",
                      width=2, height=2,
                      bg="white", fg="black",)
button_4 = Button(root, text="/",
                      width=2, height=2,
                      bg="white", fg="black",)
button_5 = Button(root, text="%",
                      width=2, height=2,
                      bg="white", fg="black",)
button_6 = Button(root, text="**",
                      width=2, height=2,
                      bg="white", fg="black",)
button_7 = Button(root, text="//",
                      width=2, height=2,
                      bg="white", fg="black",)
button_8 = Button(root, text="=",
                      width=2, height=2,
                      bg="white", fg="black",)
#number
button_n1 = Button(root, text="1",
                      width=1, height=1,
                      bg="white", fg="black",)
button_n2 = Button(root, text="2",
                      width=1, height=1,
                      bg="white", fg="black",)
button_n3 = Button(root, text="3",
                      width=1, height=1,
                      bg="white", fg="black",)
button_n4 = Button(root, text="4",
                      width=1, height=1,
                      bg="white", fg="black",)
button_n5 = Button(root, text="5",
                      width=1, height=1,
                      bg="white", fg="black",)
button_n6 = Button(root, text="6",
                      width=1, height=1,
                      bg="white", fg="black",)
button_n7 = Button(root, text="7",
                      width=1, height=1,
                      bg="white", fg="black",)
button_n8 = Button(root, text="8",
                      width=1, height=1,
                      bg="white", fg="black",)
button_n9 = Button(root, text="9",
                      width=1, height=1,
                      bg="white", fg="black",)
button_n0 = Button(root, text="0",
                      width=1, height=1,
                      bg="white", fg="black",)

entry = Entry(root, width=70)
entry.grid()


button_1.grid(row=1,column=1,sticky='w')
button_2.grid(row=1,column=0)
button_3.grid()
button_4.grid()
button_5.grid()
button_6.grid()
button_7.grid()
button_8.grid()
button_n1.grid()
button_n2.grid()
button_n3.grid()
button_n4.grid()
button_n5.grid()
button_n6.grid()
button_n7.grid()
button_n8.grid()
button_n9.grid()
button_n0.grid()


root.mainloop()