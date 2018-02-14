"""
When you use setup and teardown functions, pytest will run setup before tests
and teardown after tests.

To see a step by step, run the command line 'pytest -v[all_files] -s[step_by_step]'
"""
import pytest



def setup_module(module):
    print("Setting up Module")

def teardown_module(module):
    print("Tearing down Module")



def setup_function(function):
    if function == test1:
        print("\nSetting up test1")
    elif function == test2:
        print("\nSetting up test2")
    else:
        print("\nSetting up unknown test")

def teardown_function(function):
    if function == test1:
        print("\nTearing down test1")
    elif function == test2:
        print("\nTearing down test2")
    else:
        print("\nTearing down unknown test")


def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True
