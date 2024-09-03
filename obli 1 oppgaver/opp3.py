from operator import length_hint
from tkinter import *
from unittest.mock import right

root = Tk()
root.geometry("400x400")
root.title('Kalko')

#operatorer
button_1 = Button(root, text="+",
                      width=1, height=1,
                      bg="white", fg="black",)
button_2 = Button(root, text="-",
                      width=1, height=1,
                      bg="white", fg="black",)
button_3 = Button(root, text="*",
                      width=1, height=1,
                      bg="white", fg="black",)
button_4 = Button(root, text="/",
                      width=1, height=1,
                      bg="white", fg="black",)
button_5 = Button(root, text="%",
                      width=1, height=1,
                      bg="white", fg="black",)
button_6 = Button(root, text="**",
                      width=1, height=1,
                      bg="white", fg="black",)
button_7 = Button(root, text="//",
                      width=1, height=1,
                      bg="white", fg="black",)
button_8 = Button(root, text="=",
                      width=1, height=1,
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
entry.pack(padx=1, pady=1,)


button_1.pack(side=LEFT)
button_2.pack(side=LEFT)
button_3.pack(side=LEFT)
button_4.pack(side=LEFT)
button_5.pack(side=LEFT)
button_6.pack(side=LEFT)
button_7.pack(side=LEFT)
button_8.pack(side=LEFT)
button_n1.pack()
button_n2.pack()
button_n3.pack()
button_n4.pack()
button_n5.pack()
button_n6.pack()
button_n7.pack()
button_n8.pack()
button_n9.pack()
button_n0.pack()


root.mainloop()