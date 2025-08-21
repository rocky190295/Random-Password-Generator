import pytest
from src.cli_main import generate_password

def test_zero_length():
    with pytest.raises(ValueError):
        generate_password(0, True, True, True, True)

def test_large_length():
    pwd = generate_password(1000, True, True, True, True)
    assert len(pwd) == 1000

def test_randomness_across_runs():
    results = [generate_password(12, True, True, True, True) for _ in range(10)]
    assert all(len(p) == 12 for p in results)
    assert len(set(results)) > 1  # basic randomness check