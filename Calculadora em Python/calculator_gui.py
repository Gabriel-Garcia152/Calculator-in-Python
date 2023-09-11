import tkinter as tk
from calculator_logic import Calculator

calculator = Calculator()

class MyCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.label = tk.Label(root, text="Ready to calculate!", bg='gray')
        self.label.grid(row=0, column=0, columnspan=3)

        buttons = [
            "1", "2", "3", "+",
            "4", "5", "6", "-",
            "7", "8", "9", "*",
            "0", "=", "/", "C"
        ]

        row, col = 1, 0

        for button_text in buttons:
            tk.Button(root, text=button_text, command=lambda t=button_text: self.on_button_click(t), width="5", height="2", bg="gray").grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, text):
        self.text = text

        if text == "=":
            calculator.perform_calculator()
            self.label.config(text=calculator.result, bg="gray")
        else:
            calculator.update(text)
            self.label.config(text=" ".join(map(str,calculator.display)), bg="gray")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="gray")
    root.geometry("250x300")
    app = MyCalculator(root)
    root.mainloop()
