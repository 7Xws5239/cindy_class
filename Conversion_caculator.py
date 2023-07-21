import tkinter as tk
from tkinter import messagebox

def validate_input():
    value = entry.get()
    from_base = var_from.get()

    if from_base == 'Binary':
        if not all(c in '01' for c in value):
            return False
    elif from_base == 'Decimal':
        if not value.isdigit():
            return False
    elif from_base == 'Hexadecimal':
        if not all(c in '0123456789abcdefABCDEF' for c in value):
            return False

    return True

def convert():
    if not validate_input():
        messagebox.showerror('Error', 'Invalid input for the selected base')
        return

    value = entry.get()
    from_base = var_from.get()
    to_base = var_to.get()

    # Convert the input value to decimal
    if from_base == 'Binary':
        value = int(value, 2)
    elif from_base == 'Decimal':
        value = int(value)
    elif from_base == 'Hexadecimal':
        value = int(value, 16)

    # Convert the decimal value to the desired base
    if to_base == 'Binary':
        result = bin(value)[2:]
    elif to_base == 'Decimal':
        result = str(value)
    elif to_base == 'Hexadecimal':
        result = hex(value)[2:]

    label_result.config(text='Result: ' + result)

window = tk.Tk()
window.title("Base Conversion Calculator")

entry = tk.Entry(window, width=30)
entry.grid(row=0, column=1)

bases = ['Binary', 'Decimal', 'Hexadecimal']

var_from = tk.StringVar()
var_from.set(bases[0])

var_to = tk.StringVar()
var_to.set(bases[0])

option_from = tk.OptionMenu(window, var_from, *bases)
option_from.grid(row=0, column=0)

option_to = tk.OptionMenu(window, var_to, *bases)
option_to.grid(row=1, column=0)

button_convert = tk.Button(window, text='Convert', command=convert)
button_convert.grid(row=2, column=0, columnspan=2)

label_result = tk.Label(window, text='Result: ')
label_result.grid(row=3, column=0, columnspan=2)

window.mainloop()
