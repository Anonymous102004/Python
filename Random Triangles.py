from tkinter import *
import random

root = Tk()


# Menu Bar Config
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
subMenu = Menu(menu, tearoff=0) # Removes Hashed Line
menu.add_cascade(label="File", menu=subMenu)


# Menu Bar Items
subMenu.add_command(label="Reset") # Not Implemented!
subMenu.add_separator() # --- (separator) ---                          
subMenu.add_command(label="Exit", command=quit)


# Main Canvas
canvas = Canvas(root, width=500, height=500)
canvas.pack()


# Line Randomizer X Y Z
for x in range(1):
    x = random.randint(1, 300) # Default is 1,101
    print ("X equals", x)

for y in range(1):
    y = random.randint(1, 300)
    print ("Y equals", y)

for z in range(1):
    z = random.randint(1, 300)
    print ("Z equals", z)

# Lines X Y Z  
xLines = canvas.create_line(x, y, z, x) # X, Y, Z, X 
yLines = canvas.create_line(y, z, x, y) # Y, Z, X, Y
yLines = canvas.create_line(z, x, y, z) # Z, X, Y, Z


# Repeats the Program
root.mainloop()




