# test_square.py
import math


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_square():
    assert 7 * 7 == 40


def test_equality():
    assert 10 == 11
