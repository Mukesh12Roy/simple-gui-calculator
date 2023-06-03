import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    tk.Button(window, text=button, width=7, command=lambda button=button: entry.insert(tk.END, button)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(window, text="Clear", width=7, command=clear).grid(row=row, column=col, columnspan=2)
tk.Button(window, text="Calculate", width=15, command=calculate).grid(row=row, column=col+2, columnspan=2)

window.mainloop()

