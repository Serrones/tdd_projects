"""
pytest.fixture() give us a way to create initializers whitout the help of setup.

"""

import pytest


#It's similar to a setup
@pytest.fixture(autouse=True)# This way the pytest.fixture will act in every function
def setup():
    print("\n Setup")

def test1():# If you put "setup" as a param, it will use pytest.fixture only this function
    print("Executing Test1")
    assert True

# @pytest.mark.usefixtures("setup") -- Another way to call pytest.fixture
def test2():
    print("Executing Test2")
    assert True
