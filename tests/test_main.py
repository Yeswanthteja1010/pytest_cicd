from app import main

def test_add():
  assert main.add(2,5) == 7

def test_subtract():
  assert main.subtract(10, 4) == 6
  
