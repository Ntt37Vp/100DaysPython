import tkinter

# create the window Tk
window = tkinter.Tk()
window.title("My First Tkinter program")
window.minsize(width=500, height=400)

# Label
mylabel = tkinter.Label(text="Hi! I am a label", font=("Arial", 24, "bold"))
mylabel.pack()
# mylabel.pack(side="left")
# OR use
# mylabel.config(text="New Text")

# Button
# button = tkinter.Button(text="click me")
# button.pack()

# Using COMMAND arg to call a func like event listener
def button_clicked():
    print("I got clicked")
    mylabel.config(text="Button got clicked")


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry (like input)
input = tkinter.Entry(width=25)
input.pack()
input.get()

# keep it open on a loop; add it at the end
window.mainloop()