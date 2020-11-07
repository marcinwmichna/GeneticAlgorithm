from tkinter import *
from calc.test_calc import *
from PIL import ImageTk, Image

app = Tk()

img = ImageTk.PhotoImage(Image.open(r"img/function.jpg"))
functionLabel = Label(app, image=img)
functionLabel.pack()

# zakres X
Xfrom_label = Label(app, text="X from:")
Xfrom_label.pack()
Xfrom = Entry(app, width=60, borderwidth=5)
Xfrom.pack()
Xto_label = Label(app, text="X to:")
Xto_label.pack()
Xto = Entry(app, width=60, borderwidth=5)
Xto.pack()

# populacja
population_label = Label(app, text="population")
population_label.pack()
pupulation_input = Entry(app, width=60, borderwidth=5)
pupulation_input.pack()

# epoki
epoch_label = Label(app, text="epoch")
epoch_label.pack()
epoch_input = Entry(app)
epoch_label.pack()

# wynik
output1 = Entry(app, width=60, borderwidth=5)
output1.pack()


multiply_button = Button(app, text="multiply",
                         command=lambda: multiplay_click())
multiply_button.pack()
app.mainloop()


def multiplay_click():
    value1 = Xfrom.get()
    value2 = Xto.get()
    print("value: ", value1, "value2: ", value2)
    result = multiply(int(value1), int(value2))
    output1.delete(0, END)
    output1.insert(0, str(result))
