"""
With params defined, we can run pytest fixture and unit test with all params
passed

"""



import pytest

@pytest.fixture(params=[1, 2, 3])
def setup(request):
    value = request.param
    print('\nSetup! - value = {}'.format(value))
    return value

def test1(setup):
    print('\nSetup = {}'.format(setup))
    assert True
