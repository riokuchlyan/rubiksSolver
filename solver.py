import tkinter as tk

side1=[["red", "red", "red"],["red", "red", "red"],["red", "red", "red"]]
side2=[["orange", "orange", "orange"],["orange", "orange", "orange"],["orange", "orange", "orange"]]
side3=[["yellow", "yellow", "yellow"],["yellow", "yellow", "yellow"],["yellow", "yellow", "yellow"]]
side4=[["white", "white", "white"],["white", "white", "white"],["white", "white", "white"]]
side5=[["blue", "blue", "blue"],["blue", "blue", "blue"],["blue", "blue", "blue"]]
side6=[["green", "green", "green"],["green", "green", "green"],["green", "green", "green"]]

window=tk.Tk()
window.geometry("800x800")
window.title("Rubiks Solver")

canvas=tk.Canvas(window, width=800, height=800)
canvas.pack()

#for row in range(3):
#    for col in range(3):
 #       canvas.create_rectangle(row*10,col*10,row*20,col*20, fill="red", outline="black")


window.mainloop()


"""
x1=100
x2=300
y1=100
y2=300
canvas.create_rectangle(x1,y1,x2,y2,fill="red",outline="black")
window.mainloop()
"""
#table = tk.Frame(window)
#for row in range(3):
#    for col in range(3):
#        label = tk.Label(table, text="")
#        label.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
#        table[(row, col)] = label

tk.mainloop()