import pytest

#prod code
def str_len(theStr):
    p = len(theStr)
    return p

#unit testing
def test_str_length():
    theStr = "1"
    result = str_len(theStr)
    assert result == 1