import tkinter
import random
canvas = tkinter.Canvas(height = 800, width = 1200, background="white")
x = 50
y = 50
x1 = 100
y1 = 100
canvas.pack()
farba = ["navy","red","magenta","purple"]
farba1 = random.choice(farba)
def kresli_kvetinu():
    global x, y, x1, y1, farba1
    canvas.create_oval(x-25, y-25, x1-25, y1-25, fill=farba1)
    canvas.create_oval(x+25, y+25, x1+25, y1+25, fill=farba1)
    canvas.create_oval(x-25, y+25, x1-25, y1+25, fill=farba1)
    canvas.create_oval(x+25, y-25, x1+25, y1-25, fill=farba1)
    canvas.create_oval(x, y, x1, y1, fill="yellow")
    canvas.create_polygon(x + 8, y1 - 8, x1 - 25, y, x1 - 8, y1 - 8, x + 2, y + 16, x + 49, y + 16, x + 8, y1 - 8, fill="white", outline = "black")
def kresli_rad():
    global x, y, x1, y1, farba1
    for i in range (11):
        kresli_kvetinu()
        x = x + 105
        x1 = x1 + 105
        farba1 = random.choice(farba)
for i in range (7):
    x = 50
    x1 = 100
    kresli_rad()
    y = y + 105
    y1 = y1 + 105
canvas.mainloop()