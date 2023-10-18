import tkinter
canvas = tkinter.Canvas(width = 800, height = 650, background = "white")
canvas.pack()
#Pismeno J
canvas.create_line(50,50,100,50,100,100)
canvas.create_arc(50,50, 100, 150,start = 180, extent = 180)
canvas.create_line(51,100,100,100, fill = "white")

#Pismeno A
canvas.create_line(125,150,150,50, fill = "blue", width = 3)
canvas.create_line(150,40,170,20, fill = "blue", width = 3)
canvas.create_line(150,50,175,150, fill = "blue", width = 3)
canvas.create_line(138 ,100, 163, 100, fill = "blue", width = 3)

#Pismeno N
canvas.create_line(200, 150, 200, 50, 250, 150, 250, 50, fill = "green", width = 7)

#Pismeno B
canvas.create_arc(350,50, 400, 100, start = 270, extent = 180, width = 6, outline = "orange")
canvas.create_arc(350,100,400, 150, start = 270, extent = 180, width = 6, outline = "orange")

#Pismeno O
canvas.create_oval(425, 50, 450, 150, outline= "red", width = 10)

#Pismeno S
canvas.create_arc(475,50, 525, 100, start = 75, extent = 180, width = 1, outline = "brown",style=tkinter.ARC)
canvas.create_arc(460,98, 513, 150, start = 255, extent = 180, width = 1, outline = "brown",style=tkinter.ARC)

#Pismeno A
canvas.create_line(525,150,550,50, fill = "yellow", width = 7)
canvas.create_line(550,50,575,150, fill = "yellow", width = 7)
canvas.create_line(538 ,100, 565, 100, fill = "yellow", width = 7)
canvas.create_line(550,40,585,20, fill = "yellow", width = 7)
#Pismeno K
canvas.create_line(590, 50, 590, 150, fill = "purple", width = 15)
canvas.create_line(590, 100, 645, 50, fill = "purple", width = 15)
canvas.create_line(590, 100, 645, 150, fill = "purple", width = 15)
