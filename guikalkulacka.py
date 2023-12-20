from tkinter import *
import math

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)

        expression = ""
    except:

        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def Pow():
    global expression
    try:
        result = math.pow(eval(expression), 2)

        expression = str(result)
        equation.set(expression)
    except:
        equation.set(" error ")
        expression = ""

def squareRoot():
    global expression
    try:
        result = math.sqrt(eval(expression))

        expression = str(result)
        equation.set(expression)
    except:
        equation.set(" error ")
        expression = ""

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="yellow")
    gui.title("Simple Calculator")

    screen_width = gui.winfo_screenwidth()
    screen_height = gui.winfo_screenheight()


    gui.geometry( "1920x1080")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan = 20, ipadx = 100)

    button1 = Button(gui, text = ' 1 ', fg = 'black', bg='red', command=lambda: press(1), height=1,width=7)
    button1.grid(row = 2, column = 0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=1)

    plus = Button(gui, text = ' + ', fg='black',bg='red',command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=2, column=4)

    multiply = Button(gui, text=' * ', fg='black', bg='red', command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=3, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red', command=lambda: press("/"), height=1, width=7)
    divide.grid(row=3, column=4)

    SquareRoot = Button(gui, text=' √ ', fg='black', bg='red', command=squareRoot, height=1, width=7)
    SquareRoot.grid(row=4, column=3)

    Power = Button(gui, text=' ^2 ', fg='black', bg='red', command=Pow, height=1, width=7)
    Power.grid(row=4, column=4)

    equal = Button(gui, text=' = ', fg='black', bg='red', command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text=' clear ', fg='black', bg='red', command=clear, height=1, width=7)
    clear.grid(row=5, column=3)

    Decimal = Button(gui, text=' . ', fg='black', bg='red', command=lambda: press("."), height=1, width=7)
    Decimal.grid(row=5, column=0)

    gui.mainloop()