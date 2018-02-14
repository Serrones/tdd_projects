"""
Here we will verify the importance of the 'test' word in name's position.

"""

import pytest

class TestClass:
    def test_me(self):
        assert True

    def test_me2(self):
        assert True


# Remember, pytest only recognyzes classes with "Test"  at the beggining name
class ClassTest:
    def test_me(self):
        assert True

    def test_me2(self):
        assert True




def test_me():
    assert True

def test_me2():
    assert True

# Remember, pytest only recognyzes functions with "test_"  at the beggining name
def not_a_test():
    assert True
