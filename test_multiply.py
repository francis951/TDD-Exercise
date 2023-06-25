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
from multiply import multiply_one

"""
the module to do the test
"""


def test_multiply_one():
    """
    the check for the assert
    """

    assert multiply_one(1, 1) == 1
    assert multiply_one(2, 2) == 4
    assert multiply_one(3, 3) == 9
    assert multiply_one(4, 4) == 16
    assert multiply_one(23, 45) == 1035
