from pytest import approx

def test_int_assert():
    assert 1 == 1

def test_str_assert():
    assert "str" == "str"

def test_float_assert():
    assert 1.0 == 1.0

def test_array_assert():
    assert [1, 2, 3] == [1, 2, 3]

def test_dict_assert():
    assert {1, 2, 3} == {1, 2, 3}

# In the following test, it fails because internally python calculates
# float numbers in a bit mode, giving different results
def test_float_assert():
    assert (0.1 + 0.2) == 0.3

# To avoid this problem, you can use aprox() to compare the aproximate results
def test_approx_float_assert():
    assert (0.1 + 0.2) == approx(0.3)
