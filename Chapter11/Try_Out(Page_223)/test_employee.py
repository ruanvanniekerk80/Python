import pytest
from employee import Employee

@pytest.fixture
def employee_instance():
    """A fixture that provides an Employee instance for tests."""
    return Employee('John', 'Doe', 50000)

def test_give_default_raise(employee_instance):
    """Test using the fixture for a default raise."""
    employee_instance.give_raise()
    assert employee_instance.salary == 55000

def test_give_custom_raise(employee_instance):
    """Test using the fixture for a custom raise."""
    employee_instance.give_raise(10000)
    assert employee_instance.salary == 60000