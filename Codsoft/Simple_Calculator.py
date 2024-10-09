import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Create and place labels and entry fields
        self.num1_label = tk.Label(root, text="Enter first number:")
        self.num1_label.pack(pady=5)

        self.num1_entry = tk.Entry(root)
        self.num1_entry.pack(pady=5)

        self.num2_label = tk.Label(root, text="Enter second number:")
        self.num2_label.pack(pady=5)

        self.num2_entry = tk.Entry(root)
        self.num2_entry.pack(pady=5)

        self.operation_label = tk.Label(root, text="Choose an operation:")
        self.operation_label.pack(pady=5)

        # Create buttons for operations
        self.add_button = tk.Button(root, text="+", command=lambda: self.calculate("add"))
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.subtract_button = tk.Button(root, text="-", command=lambda: self.calculate("subtract"))
        self.subtract_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.multiply_button = tk.Button(root, text="*", command=lambda: self.calculate("multiply"))
        self.multiply_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.divide_button = tk.Button(root, text="/", command=lambda: self.calculate("divide"))
        self.divide_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero.")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
