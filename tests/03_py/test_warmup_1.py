import warmup_1.py
from warmup_1.py import sleep_in

def test_sleep_in(weekday, vacation):
  assert sleep_in(False, False) == True
  assert sleep_in(True, False) == False
  assert sleep_in(False, True) == True
  assert sleep_in(True, True) == True