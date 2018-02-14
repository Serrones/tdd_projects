"""
Pytest doesn't recognize this file when you run the command "pytest -v".
It's because Pytest only recognizes files with "test" at the beggining or ending
 in the file name.
"""

import pytest

def test_me():
    assert True

def test_me2():
    assert True
