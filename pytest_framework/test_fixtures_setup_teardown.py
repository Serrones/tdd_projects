"""
pytest.fixture() give us 02 Ways to create initializers and finalizers
whitout the help of setup and teardown.

The first one is using "yeld" - For a single return

The second is using request.addfinalizer() - For n differents returns

"""


import pytest


#It's similar to a setup and teardown - just using the yield
@pytest.fixture()# "autouse=True" This way the pytest.fixture will act in every function
def setup1():
    print("\n Setup 1")
    yield
    print('\n TearDown 1')

#Whitout yield, you need to use request.addfinalizer
@pytest.fixture()
def setup2(request):
    print("\n Setup 2")

    def teardown_a():
        print('\n TearDown A')

    def teardown_b():
        print('\n TearDown B')


    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):# If you put "setup1" as a param, it will use pytest.fixture only this function
    print("Executing Test1")
    assert True

def test2(setup2):
    print("Executing Test2")
    assert True
