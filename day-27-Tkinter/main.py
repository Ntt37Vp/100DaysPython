import tkinter

# create the window Tk
window = tkinter.Tk()
window.title("My First Tkinter program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    mylabel.config(text=new_text)


# Label
mylabel = tkinter.Label(text="Hi! I am a label", font=("Arial", 24, "bold"))
mylabel.config(text="New text")
# mylabel.pack()
# mylabel.place(x=250, y=100)
mylabel.grid(column=0, row=0) # first column first row

# Button
button = tkinter.Button(text="click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry (like input)
input = tkinter.Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)

# Other widgets
# Text, Spinbox, Scale (slider), Checkbutton, Radiobutton, Listbox


# keep it open on a loop; add it at the end
window.mainloop()
