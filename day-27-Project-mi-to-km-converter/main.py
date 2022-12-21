import tkinter

# create the window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


# calculate function ; 1.609344
def convert_mi_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609344)
    km_result.config(text=f"{km}")


# Entry
miles_input = tkinter.Entry(width=9)
print(miles_input.get())
miles_input.grid(column=1, row=0)

# Button
button = tkinter.Button(text="Calculate", command=convert_mi_km)
button.grid(column=1, row=2)

# Label - Miles
miles_label = tkinter.Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=2, row=0)

# Label - equal to
equal_to_label = tkinter.Label(text="is equal to", font=("Arial", 24))
equal_to_label.grid(column=0, row=1)

# Label - Result
km_result = tkinter.Label(text="0", font=("Arial", 24))
km_result.grid(column=1, row=1)

# Label - Km
km_label = tkinter.Label(text="Km", font=("Arial", 24))
km_label.grid(column=2, row=1)

# keep the window open in a loop
window.mainloop()
