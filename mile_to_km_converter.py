from tkinter import *

window = Tk()
window.title("Mile to Kilometer converter")
window.config(padx=20, pady=20)
# label
miles_label = Label(text="miles")
miles_label.grid(row=1, column=2)
Km_label = Label(text="Kilometer")
Km_label.grid(row=2, column=2)
my_label = Label(text="is equal to", font=("Ariel", 10,))
my_label.grid(row=2, column=0)


def convert():

    miles = float(input.get())
    km = miles*1.61
    output.config(text=f"{km}")


# my_label.config(text="new text")


button = Button(text="Calculate", command=convert)
button.grid(row=3, column=1)
output = Label(text="convert", width=10)
output.grid(row=2, column=1)
# entry
input = Entry(width=8)
input.grid(row=1, column=1)




window.mainloop()
