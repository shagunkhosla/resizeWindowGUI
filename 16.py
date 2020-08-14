from tkinter import *



root= Tk()
root.geometry("500x500")
root.title("Window Resizer")
Label(text="Window Resizer", font="comicsansms 11 bold", pady=20).grid(column=2)

def hello():
    print(f"height is {height_var.get()}  width is {width_var.get()} ")
    root.geometry(f"{width_var.get()}x{height_var.get()}")

height_var=StringVar()
width_var=StringVar()

height_entry=Entry(root, textvariable=height_var)
width_entry=Entry(root, textvariable=width_var)

Label(root, text="Enter Height: ").grid(row=1, column=0)
height_entry.grid(row=1, column=1)

Label(root, text="Enter Width: ",padx=10, pady=10).grid()
width_entry.grid(row=2,column=1)

b1=Button(root, text="Apply Changes",padx=10, pady=10, command=hello)
b1.grid(column=1)
root.mainloop()