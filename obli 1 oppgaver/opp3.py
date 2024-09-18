from tkinter import *


root = Tk()
root.geometry("500x500")
root.title('Kalko')
root.configure(background='black')

equation_text = ""

E_label = StringVar()


L = Label(root, textvariable=E_label, width=45, height=3, bg="black", fg="white", anchor="e", font=("Arial", 14))
L.grid(row=0, column=0, columnspan=4)

def add_to_equation(symbol):
    global equation_text
    equation_text += str(symbol)
    E_label.set(equation_text)


def evaluate_equation():
    global equation_text
    try:
        result = str(eval(equation_text))
        E_label.set(result)
        equation_text = result
    except Exception as e:
        E_label.set("Error")
        equation_text = ""


def clear():
    global equation_text
    equation_text = ""
    E_label.set("")


button_clear = Button(root, text="C", width=9, height=4, bg="red", fg="white", command=clear)
button_1 = Button(root, text="+", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation("+"))
button_2 = Button(root, text="-", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation("-"))
button_3 = Button(root, text="*", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation("*"))
button_4 = Button(root, text="/", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation("/"))
button_5 = Button(root, text="%", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation("%"))
button_6 = Button(root, text="**", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation("**"))
button_7 = Button(root, text="//", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation("//"))
button_8 = Button(root, text="=", width=9, height=4, bg="black", fg="white", command=evaluate_equation)


button_n1 = Button(root, text="1", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation(1))
button_n2 = Button(root, text="2", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation(2))
button_n3 = Button(root, text="3", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation(3))
button_n4 = Button(root, text="4", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation(4))
button_n5 = Button(root, text="5", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation(5))
button_n6 = Button(root, text="6", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation(6))
button_n7 = Button(root, text="7", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation(7))
button_n8 = Button(root, text="8", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation(8))
button_n9 = Button(root, text="9", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation(9))
button_n0 = Button(root, text="0", width=9, height=4, bg="black", fg="white", command=lambda: add_to_equation(0))


button_clear.grid(row=1, column=0)
button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)
button_3.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=2, column=3)

button_8.grid(row=3, column=3)

button_n1.grid(row=3, column=0)
button_n2.grid(row=3, column=1)
button_n3.grid(row=3, column=2)

button_n4.grid(row=4, column=0)
button_n5.grid(row=4, column=1)
button_n6.grid(row=4, column=2)

button_n7.grid(row=5, column=0)
button_n8.grid(row=5, column=1)
button_n9.grid(row=5, column=2)
button_n0.grid(row=5, column=3)

root.mainloop()
