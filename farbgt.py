import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def rgb(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
def stvorec(strana, x, y, farba=''):
    canvas.create_rectangle(x, y, x+strana, y+strana, fill=farba)
for i in range(10):
    stvorec(30, i*30, 10, rgb(100+16*i, 0, 0))
    stvorec(30, i*30, 50, rgb(100+16*i, 0, 255-26*i))
    stvorec(30, i*30, 90, rgb(26*i, 26*i, 26*i))
    stvorec(30, i*30, 130, rgb(0, 26*i, 26*i))
canvas.mainloop()