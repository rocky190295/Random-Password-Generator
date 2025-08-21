import pytest

@pytest.fixture
def password_file(tmp_path):
    return tmp_path / "saved_passwords.txt"