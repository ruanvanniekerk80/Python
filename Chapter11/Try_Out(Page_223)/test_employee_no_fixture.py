from employee import Employee

def test_give_default_raise():
    """Test that a default raise of $5,000 works."""
    emp = Employee('John', 'Doe', 50000)
    emp.give_raise()
    assert emp.salary == 55000

def test_give_custom_raise():
    """Test that a specific raise amount works."""
    emp = Employee('John', 'Doe', 50000)
    emp.give_raise(10000)
    assert emp.salary == 60000