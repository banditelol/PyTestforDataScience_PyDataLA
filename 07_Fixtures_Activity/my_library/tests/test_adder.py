"""Add tests for adders here """
import pytest
from .. import my_module

@pytest.fixture(scope="session")
def single_object_fixture():
    single_object = my_module.SingleObject(0)
    return single_object

def test_value_zero(single_object_fixture):
    assert single_object_fixture.number == 0

def test_add_zero(single_object_fixture):
    result = single_object_fixture.add_more(0)
    assert result == 0

def test_add_pos(single_object_fixture):
    num1 = 9999
    result = single_object_fixture.add_more(num1)
    assert result == 9999

def test_add_neg(single_object_fixture):
    num1 = -9999
    result = single_object_fixture.add_more(num1)
    assert result == -9999