import tkinter as tk
from tkinter import messagebox
from .cli_main import generate_password, save_password


def on_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a positive integer for length.")
        return

    password = generate_password(
        length,
        upper_var.get(),
        lower_var.get(),
        digits_var.get(),
        symbols_var.get()
    )

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, password)

    if save_var.get():
        save_password(password)

def on_copy():
    password = result_box.get("1.0", tk.END).strip()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Keeps clipboard after window closes
        messagebox.showinfo("Copied", "Password copied to clipboard.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x400")
root.resizable(False, False)

# Input: Length
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

# Options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)
save_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Save to File", variable=save_var).pack(anchor='w', padx=20)

# Buttons
tk.Button(root, text="Generate Password", command=on_generate).pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=on_copy).pack()

# Output: Multi-line Text Box
result_box = tk.Text(root, height=4, width=50, wrap="word")
result_box.pack(pady=10)

root.mainloop()