from tkinter import *
from calc.test_calc import *

app = Tk()


input1 = Entry(app, width=100, borderwidth=5)
input1.pack()
input2 = Entry(app, width=100, borderwidth=5)
input2.pack()

output1 = Entry(app, width=100, borderwidth=5)
output1.pack()


def multiplay_click():
    value1 = input1.get()
    value2 = input2.get()
    print("value: ", value1, "value2: ", value2)
    result = multiply(int(value1), int(value2))
    output1.delete(0, END)
    output1.insert(0, str(result))


multiply_button = Button(app, text="multiply",
                         command=lambda: multiplay_click())
multiply_button.pack()
app.mainloop()
