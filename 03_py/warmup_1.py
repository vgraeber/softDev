def sleep_in(weekday, vacation):
  if ((vacation == True) or (weekday == False)):
    return True
  else:
    return False

def test_sleep_in(weekday, vacation):
  assert sleep_in(False, False) == True
  assert sleep_in(True, False) == False
  assert sleep_in(False, True) == True
  assert sleep_in(True, True) == True

def monkey_trouble(a_smile, b_smile):
  if (a_smile == b_smile):
    return True
  else:
    return False

def sum_double(a, b):
  if (a != b):
    return (a + b)
  else:
    return ((a + b) * 2)

def diff21(n):
  if (n > 21):
    return (2 * (abs(21 - n)))
  else:
    return (abs(21 - n))

def parrot_trouble(talking, hour):
  if ((talking == True) and ((hour < 7) or (hour > 20))):
    return True
  else:
    return False

def makes10(a, b):
  if ((a == 10) or (b == 10)):
    return True
  elif ((a + b) == 10):
    return True
  else:
    return False

def near_hundred(n):
  if ((abs(100 - n) <= 10) or (abs(200 - n) <= 10)):
    return True
  else:
    return False

def pos_neg(a, b, negative):
  if (negative):
    return ((a < 0) and (b < 0))
  return ((a * b) < 0)

def not_string(str):
  if (str[0:3] == 'not'):
    return str
  else:
    str2 = 'not ' + str
    return (str2)

def missing_char(str, n):
  str2 = (str[:n] + str[(n + 1):])
  return str2

def front_back(str):
  if (len(str) <= 1):
    return str
  else:
    str2 = str[-1] + str[1:-1] + str[0]
    return str2

def front3(str):
  str2 = (str[0:3] * 3)
  return str2