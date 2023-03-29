from 03_py import warmup_1

def test_sleep_in(weekday, vacation):
  assert sleep_in(False, False) == True
  assert sleep_in(True, False) == False
  assert sleep_in(False, True) == True
  assert sleep_in(True, True) == True