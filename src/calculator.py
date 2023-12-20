# calculator.py
def add(a, b):
  checkInputs(a,b)
  return a+b
def subtract(a, b):
  checkInputs(a,b)
  return a-b
def multiply(a,b):
  checkInputs(a,b)
  return a*b
def divide(a,b):
  checkInputs(a,b)
  return a/b
def checkInputs(a,b):
  if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
    raise TypeError("Inputs must be either int or float!")

# test_addition.py
from src.calculator import add
import pytest
def test_add():
  result=add(3,4)
  assert result==7
def test_add_string():
  with pytest.raises(TypeError):
    add("string",4)


