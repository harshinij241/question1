from app import multiply, divide
import pytest

def test_multiply():
    assert multiply(5,3)==16

def test_divide():
    assert divide(4,2)==2   
