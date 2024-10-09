import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Create UI elements
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.lowercase_var = tk.BooleanVar(value=True)
        self.lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_checkbox.pack()

        self.uppercase_var = tk.BooleanVar(value=True)
        self.uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_checkbox.pack()

        self.digits_var = tk.BooleanVar(value=True)
        self.digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=self.digits_var)
        self.digits_checkbox.pack()

        self.special_var = tk.BooleanVar(value=False)
        self.special_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=self.special_var)
        self.special_checkbox.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack()

        self.password_display = tk.Entry(root, width=50)
        self.password_display.pack()

    def generate_password(self):
        length = self.length_entry.get()
        if not length.isdigit() or int(length) < 8:
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, "Length must be at least 8.")
            return
        
        length = int(length)
        characters = ''
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.digits_var.get():
            characters += string.digits
        if self.special_var.get():
            characters += string.punctuation

        if not characters:
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, "Select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

