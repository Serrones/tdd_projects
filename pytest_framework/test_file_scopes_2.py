"""

Different scopes for pytest.fixture

- module

- class

- function

"""

import pytest

@pytest.fixture(scope="module", autouse=True)
def setup_module2():
    print('\nSetup Module2')

@pytest.fixture(scope="class", autouse=True)
def setup_class2():
    print('\nSetup Class2')

@pytest.fixture(scope="function", autouse=True)
def setup_function2():
    print('\nSetup Function2')


class TestClass:
    def test_it(self):
        print('Test It!')
        assert True

    def test_it2(self):
        print('Test It2!')
        assert True
