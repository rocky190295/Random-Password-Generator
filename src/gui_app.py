import tkinter as tk
from tkinter import ttk, messagebox

from src.password_core import generate_password
from src.password_strength import check_strength
from src.file_handler import save_password


class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # ---------------------------
        # Variables
        # ---------------------------
        self.length_var = tk.IntVar(value=12)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.specials_var = tk.BooleanVar(value=True)
        self.generated_password = tk.StringVar()

        # ---------------------------
        # UI Layout
        # ---------------------------
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(
            self.root, text="Random Password Generator", font=("Arial", 16, "bold")
        )
        title_label.pack(pady=10)

        # Password length
        frame_length = ttk.Frame(self.root)
        frame_length.pack(pady=5)
        ttk.Label(frame_length, text="Password Length:").pack(side=tk.LEFT, padx=5)
        length_spin = ttk.Spinbox(
            frame_length, from_=4, to=64, textvariable=self.length_var, width=5
        )
        length_spin.pack(side=tk.LEFT)

        # Options
        options_frame = ttk.LabelFrame(self.root, text="Character Options")
        options_frame.pack(pady=10, padx=10, fill="x")

        ttk.Checkbutton(options_frame, text="Include Uppercase (A-Z)", variable=self.uppercase_var).pack(anchor="w")
        ttk.Checkbutton(options_frame, text="Include Lowercase (a-z)", variable=self.lowercase_var).pack(anchor="w")
        ttk.Checkbutton(options_frame, text="Include Digits (0-9)", variable=self.digits_var).pack(anchor="w")
        ttk.Checkbutton(options_frame, text="Include Special Characters", variable=self.specials_var).pack(anchor="w")

        # Generate button
        generate_btn = ttk.Button(self.root, text="Generate Password", command=self.generate_password_action)
        generate_btn.pack(pady=10)

        # Display generated password
        output_entry = ttk.Entry(self.root, textvariable=self.generated_password, font=("Consolas", 12), width=40)
        output_entry.pack(pady=5)

        # Buttons frame
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=5)

        copy_btn = ttk.Button(btn_frame, text="Copy", command=self.copy_to_clipboard)
        copy_btn.pack(side=tk.LEFT, padx=5)

        save_btn = ttk.Button(btn_frame, text="Save", command=self.save_password_action)
        save_btn.pack(side=tk.LEFT, padx=5)

        # Strength analysis
        self.strength_label = ttk.Label(self.root, text="Password Strength: N/A", font=("Arial", 11))
        self.strength_label.pack(pady=10)

    # ---------------------------
    # Actions
    # ---------------------------
    def generate_password_action(self):
        try:
            password = generate_password(
                length=self.length_var.get(),
                use_uppercase=self.uppercase_var.get(),
                use_lowercase=self.lowercase_var.get(),
                use_digits=self.digits_var.get(),
                use_specials=self.specials_var.get(),
            )
            self.generated_password.set(password)

            # Check strength
            analysis = check_strength(password)
            strength_text = (
                f"Length: {analysis['length']} | "
                f"Entropy: {analysis['entropy_bits']} bits | "
                f"Verdict: {analysis['verdict']}"
            )
            self.strength_label.config(text=f"Password Strength: {strength_text}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        pwd = self.generated_password.get()
        if pwd:
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

    def save_password_action(self):
        pwd = self.generated_password.get()
        if pwd:
            save_password(pwd)
            messagebox.showinfo("Saved", "Password saved to passwords.txt")
        else:
            messagebox.showwarning("Warning", "No password to save.")


# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
