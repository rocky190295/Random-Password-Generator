# Random Password Generator (V2.0.0)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

A secure, customizable **random password generator** with a Tkinter GUI.

---

##  Features

- Generate secure passwords using Python’s `secrets` module.
- Customizable length + character options.
- Password strength analysis (entropy calculation).
- Copy to clipboard / Save to file.
- GUI built with Tkinter.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rocky190295/Random-Password-Generator.git
   cd Random-Password-Generator

   ```
2. (Optional) Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To start with the GUI
   ```bash
   python main.py
   ```

## Packaging as Executable (Optional)
If you want to use it without Python installed:
   ```bash
   pip install pyinstaller
   pyinstaller --noconsole --onfile main.py
   ```
Executable will be available in the dist/ folder.


## License
The project is licensed under the MIT Licence.

## Author
Made with ❤️ by Rakshit

## Star this Repo
If you find this project useful or educational, please consider giving it a ⭐️ on GitHub!
  