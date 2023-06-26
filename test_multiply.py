# from multiply import Multiply

# """
# This is the module for doing the test
# """


# def test_multiply():
#     """
#     pytest for the product.
#     """
#     answer = Multiply(1, 1)
#     """
#     If one is multiplied by one, the answer is equal to one.
#     """
#     assert answer.multiply_one() == 1
#     #Check for multiply of two
#     answer = Multiply(2, 2)
#     assert answer.multiply_one() == 4
from multiply import multiply

"""
the module to do the test on the multiplication
"""


def test_multiply_one():
    """
    the check for the assert
    """

    assert multiply(1, 1) == 1


def test_multiply_two():
    """
    testing for product of two
    """

    assert multiply(2, 2) == 4


def test_multiply_three():
    """
    Look for product of 3
    """

    assert multiply(3, 3) == 9


def test_multiply_four():
    """
    looking for the product of four
    """
    assert multiply(4, 4) == 16


def test_multiply_finaly():
    """
    its a  fail pass test
    """
    assert multiply(23, 45) == 1035  # 23 * 45
