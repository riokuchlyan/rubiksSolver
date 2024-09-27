import tkinter as tk

side1=[["red", "red", "red"],["red", "red", "red"],["red", "red", "red"]]
side2=[["orange", "orange", "orange"],["orange", "orange", "orange"],["orange", "orange", "orange"]]
side3=[["yellow", "yellow", "yellow"],["yellow", "yellow", "yellow"],["yellow", "yellow", "yellow"]]
side4=[["white", "white", "white"],["white", "white", "white"],["white", "white", "white"]]
side5=[["blue", "blue", "blue"],["blue", "blue", "blue"],["blue", "blue", "blue"]]
side6=[["green", "green", "green"],["green", "green", "green"],["green", "green", "green"]]

window=tk.Tk()
window.geometry("1000x1000")
window.title("Rubiks Solver")

canvas=tk.Canvas(window, width=1000, height=1000)
canvas.pack()

def create3x3Grid(originX,originY,size,color):
    for row in range(3):
        for col in range(3):
            canvas.create_rectangle(originX+(col*size),originY+(row*size),originX+size+(col*size),originY+size+(row*size), fill=color, outline="black")
    
create3x3Grid(16,16,100,"red")
create3x3Grid(350,16,100,"yellow")
create3x3Grid(683,16,100,"orange")
create3x3Grid(16,350,100,"white")
create3x3Grid(350,350,100,"blue")
create3x3Grid(683,350,100,"green")

#button not visible
solveButton=tk.Button(window,text="Solve")
solveButton.pack()

window.mainloop()
