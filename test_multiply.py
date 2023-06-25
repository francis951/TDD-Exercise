from multiply import Multiply

"""
This is the module for doing the test
"""


def test_multiply():
    """
    pytest for the product.
    """
    answer = Multiply(1, 1)
    """
    If one is multiplied by one, the answer is equal to one.
    """
    assert answer.multiply_one() == 1
    #Check for multiply of two
    answer = Multiply(2, 2)
    assert answer.multiply_one() == 4
