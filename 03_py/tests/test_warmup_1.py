from 03_py.warmup_1 import *

def test_sleep_in():
  assert sleep_in(False, False) == True
  assert sleep_in(True, False) == False
  assert sleep_in(False, True) == True
  assert sleep_in(True, True) == True