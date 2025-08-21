import pytest
from src.cli_main import generate_password

def test_password_length():
    pwd = generate_password(16, True, True, True, True)
    assert len(pwd) == 16

def test_only_uppercase():
    pwd = generate_password(10, True, False, False, False)
    assert all(c.isupper() for c in pwd)

def test_only_digits():
    pwd = generate_password(8, False, False, True, False)
    assert all(c.isdigit() for c in pwd)

def test_no_char_types_selected():
    with pytest.raises(ValueError):
        generate_password(10, False, False, False, False)

def test_symbols_included():
    pwd = generate_password(20, False, False, False, True)
    assert any(c in "!@#$%^&*()_+-=[]{}|;:',.<>?/`~" for c in pwd)