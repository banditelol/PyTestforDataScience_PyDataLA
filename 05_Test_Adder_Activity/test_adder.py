import adder    

def test_adder_ex1():
    """Test Adder for some arbitrary example"""
    num1 = 1
    num2 = 5

    added = adder.add(num1, num2)

    assert added == 6

def test_adder_sub():
    """Test Adder to make sure substitution works"""
    num1 = 99
    num2 = 100

    added1 = adder.add(num1, num2)
    added2 = adder.add(num2, num1)

    assert added1 == added2

def test_adder_nest():
    """Test Adder to make sure nesting works"""
    num1 = 99
    num2 = 100
    num3 = 1

    added = adder.add(num1, adder.add(num2,num3))

    assert added == 200

def test_adder_commute():
    """Test Adder to make sure commutative works"""
    num1 = 99
    num2 = 100
    num3 = 1

    added1 = adder.add(num1, adder.add(num2,num3))
    added2 = adder.add(adder.add(num1,num2), num3)

    assert added1 == added2

def test_adder_neg():
    """Test Adder to make sure commutative works"""
    num1 = 2
    num2 = -5

    added = adder.add(num1, num2)

    assert added == -3