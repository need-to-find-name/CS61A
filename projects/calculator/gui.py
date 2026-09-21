"""Tkinter GUI for the Simple Calculator. Run: python gui.py"""

import tkinter as tk
from calculator import evaluate_expression


class CalculatorGUI:
    def __init__(self, root):
        root.title("Calculator")
        root.resizable(False, False)

        self.entry = tk.Entry(root, font=("Arial", 20), justify="right", width=18)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.entry.focus_set()

        buttons = [
            ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("<-", 5, 2), ("=", 5, 3),
        ]
        for text, r, c in buttons:
            tk.Button(root, text=text, font=("Arial", 16), width=4,
                      command=lambda t=text: self.on_button(t)
                      ).grid(row=r, column=c, padx=3, pady=3)

        root.bind("<Return>", lambda e: self.on_button("="))
        root.bind("<BackSpace>", lambda e: self.on_button("<-"))
        root.bind("<Key>", self.on_key)

    def on_key(self, event):
        if event.char in "0123456789+-*/().":
            self.entry.insert(tk.END, event.char)
            return "break"

    def on_button(self, key):
        if key == "C":
            self.entry.delete(0, tk.END)
        elif key == "<-":
            self.entry.delete(len(self.entry.get()) - 1, tk.END)
        elif key == "=":
            expr = self.entry.get()
            try:
                result = evaluate_expression(expr)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, f"Error: {e}")
        else:
            self.entry.insert(tk.END, key)


if __name__ == "__main__":
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()
