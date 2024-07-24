import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create entry fields for numbers
        self.num1_label = tk.Label(master, text="Number 1:")
        self.num1_label.grid(row=0, column=0)
        self.num1_entry = tk.Entry(master, width=20)
        self.num1_entry.grid(row=0, column=1)

        self.num2_label = tk.Label(master, text="Number 2:")
        self.num2_label.grid(row=1, column=0)
        self.num2_entry = tk.Entry(master, width=20)
        self.num2_entry.grid(row=1, column=1)

        # Create buttons for operations
        self.add_button = tk.Button(master, text="+", command=lambda: self.calculate("+"))
        self.add_button.grid(row=2, column=0)

        self.sub_button = tk.Button(master, text="-", command=lambda: self.calculate("-"))
        self.sub_button.grid(row=2, column=1)

        self.mul_button = tk.Button(master, text="*", command=lambda: self.calculate("*"))
        self.mul_button.grid(row=4, column=0)

        self.div_button = tk.Button(master, text="/", command=lambda: self.calculate("/"))
        self.div_button.grid(row=4, column=1)

        # Create label to display result
        self.result_label = tk.Label(master, text="Result:")
        self.result_label.grid(row=6, column=0)
        self.result_entry = tk.Label(master, text="", width=20)
        self.result_entry.grid(row=6, column=1)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2!= 0:
                    result = num1 / num2
                else:
                    self.result_entry.config(text="Error: Division by zero", fg="red")
                    return

            if result < 0:
                self.result_entry.config(text=str(result), fg="red")
            else:
                self.result_entry.config(text=str(result), fg="green")
        except ValueError:
            self.result_entry.config(text="Error: Invalid input", fg="red")

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()