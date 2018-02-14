"""

Different scopes for pytest.fixture

- session

- module

- function

"""

import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_session():
    print('\nSetup Session')

@pytest.fixture(scope="module", autouse=True)
def setup_module():
    print('\nSetup Module')

@pytest.fixture(scope="function", autouse=True)
def setup_function():
    print('\nSetup Function')



def test1():
    print('Executing Test 1')
    assert True

def test2():
    print('Executing Test 2')
    assert True
