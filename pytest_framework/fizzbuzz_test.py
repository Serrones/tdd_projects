"""

TDD

- Can I call FizzBuzz
- Get '1' when I pass in 1
- Get '2' when I pass in 2
- Get 'Fizz' when I pass in 3
- Get 'Buzz' when I pass in 5
- Get 'Fizz' when I pass in 6 (a multiple of 3)
- Get 'Buzz' when I pass in 10 (a multiple of 5)
- Get 'FizzBuzz' when I pass in 15 (a multiple of 3 and 5)

"""

import pytest

# This is the first function to be created in a TDD execution
# def test_canAssertTrue():
#     assert True

# Function created with TDD
def fizzbuzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return 'FizzBuzz'
        return 'Fizz'
    elif is_multiple(value, 5):
        return 'Buzz'
    else:
        return str(value)

# Assertion part transformed to function (DRI)
def checK_fizzbuzz(value, expected_value):
    value = fizzbuzz(value)
    assert value == expected_value

# Multiplicity verifier transformed to function (DRI)
def is_multiple(value, mod):
    return (value % mod) == 0

def test_give_1_returns_1():
    checK_fizzbuzz(1, '1')

def test_give_2_returns_2():
    checK_fizzbuzz(2, '2')

def test_give_3_returns_Fizz():
    checK_fizzbuzz(3, 'Fizz')

def test_give_5_returns_Buzz():
    checK_fizzbuzz(5, 'Buzz')

def test_give_6_returns_Fizz():
    checK_fizzbuzz(6, 'Fizz')

def test_give_10_returns_Buzz():
    checK_fizzbuzz(10, 'Buzz')

def test_give_15_returns_FizzBuzz():
    checK_fizzbuzz(15, 'FizzBuzz')
