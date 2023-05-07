from tkinter import Label, Scrollbar, Tk

# instantiate Tk to root
root= Tk()

# Create Label Widget
myLabel: Label = Label(root, text = "Hello World!")
myLabel2: Label = Label(root, text = "Hello Tomato!")

scrollbar: Scrollbar = Scrollbar(root)

# Placing in screen
myLabel.pack()
myLabel2.pack()
scrollbar.pack()

root.mainloop()