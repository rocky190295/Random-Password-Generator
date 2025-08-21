from src.gui_app import PasswordGeneratorGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
