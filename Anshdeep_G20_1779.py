import tkinter as tk
import math

def button_click(symbol):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + symbol)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def square_root():
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Scientific Calculator")

display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("(", 1, 3), (")", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("+", 2, 3), ("-", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3), ("/", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("Clear", 4, 3), ("Quit", 4, 4),
    ("sin", 1, 5), ("cos", 2, 5), ("tan", 3, 5), ("sqrt", 4, 5), ("^", 5, 0),
]

for button in buttons:
    text, row, col = button
    if text == "=":
        command = calculate
    elif text == "Clear":
        command = clear_display
    elif text == "Quit":
        command = root.quit
    elif text == "sqrt":
        command = square_root
    else:
        command = lambda t=text: button_click(t)
    tk.Button(root, text=text, padx=20, pady=10, command=command).grid(row=row, column=col)

def button_click(symbol):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + symbol)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def square_root():
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Scientific Calculator")

display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("(", 1, 3), (")", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("+", 2, 3), ("-", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3), ("/", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("Clear", 4, 3), ("Quit", 4, 4),
    ("sin", 1, 5), ("cos", 2, 5), ("tan", 3, 5), ("sqrt", 4, 5), ("^", 5, 0),
]

for button in buttons:
    text, row, col = button
    if text == "=":
        command = calculate
    elif text == "Clear":
        command = clear_display
    elif text == "Quit":
        command = root.quit
    elif text == "sqrt":
        command = square_root
    else:
        command = lambda t=text: button_click(t)
    tk.Button(root, text=text, padx=20, pady=10, command=command).grid(row=row, column=col)

root.mainloop()
