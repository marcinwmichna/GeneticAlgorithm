from tkinter import *
from calc.test_calc import *
from PIL import ImageTk, Image

app = Tk()

img = ImageTk.PhotoImage(Image.open(r"img/function.jpg"))
functionLabel = Label(app, image=img)
functionLabel.grid(row=0, column=0, columnspan=2)

# zakres X
Xfrom_label = Label(app, text="X from:")
Xfrom_label.grid(row=1)
Xfrom = Entry(app, width=30, borderwidth=5)
Xfrom.grid(row=1, column=1)
Xto_label = Label(app, text="X to:")
Xto_label.grid(row=2)
Xto = Entry(app, width=30, borderwidth=5)
Xto.grid(row=2, column=1)

# populacja
population_label = Label(app, text="population:")
population_label.grid(row=3)
pupulation_input = Entry(app, width=30, borderwidth=5)
pupulation_input.grid(row=3, column=1)

# epoki
epoch_label = Label(app, text="epoch:")
epoch_label.grid(row=4, column=0)
epoch_input = Entry(app, width=30, borderwidth=5)
epoch_input.grid(row=4, column=1)

# wynik
result_label = Label(app, text="result:")
result_label.grid(row=5)
result = Entry(app, width=30, borderwidth=5)
result.grid(row=5, column=1)
multiply_button = Button(app, text="calculate",
                         command=lambda: multiplay_click())
multiply_button.grid(row=6, column=0, columnspan=2)


app.title("MCCORMICK FUNCTION")
app.mainloop()


def multiplay_click():
    value1 = Xfrom.get()
    value2 = Xto.get()
    print("value: ", value1, "value2: ", value2)
    result = multiply(int(value1), int(value2))
    result.delete(0, END)
    result.insert(0, str(result))
