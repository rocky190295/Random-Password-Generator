import subprocess
import os
import pytest

def test_cli_default():
    result = subprocess.run(
        ["python", "src/cli_main.py", "--upper", "--lower", "--digits"],
        capture_output=True, text=True
    )
    assert "Generated Password:" in result.stdout

def test_cli_save(tmp_path):
    test_file = tmp_path / "saved_passwords.txt"
    os.environ["PASSWORD_FILE"] = str(test_file)  # Optional: if you refactor to support env override

    subprocess.run(
        ["python", "src/cli_main.py", "-l", "8", "--digits", "--save"],
        capture_output=True, text=True
    )

    assert test_file.exists()
    content = test_file.read_text()
    assert any(len(line.strip()) == 8 for line in content.splitlines())

def test_cli_invalid_length():
    result = subprocess.run(
        ["python", "src/cli_main.py", "-l", "-5"],
        capture_output=True, text=True
    )
    assert "Error:" in result.stdout