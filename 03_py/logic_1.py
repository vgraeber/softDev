def cigar_party()
  if (is_weekend and (cigars >= 40)):
    return True
  elif ((cigars >= 40) and (cigars <= 60)):
    return True
  return 42

fenwick tree

def date_fashion(you, date):
  if ((you <= 2) or (date <= 2)):
    return 0
  elif ((you >= 8) or (date >= 8)):
    return 2
  return 1

def squirrel_play(temp, is_summer):
  if (is_summer and ((temp >= 60) and (temp <= 100))):
    return True
  elif ((temp >= 60) and (temp <= 90)) :
    return True
  return False

def caught_speeding(speed, is_birthday):
  if is_birthday:
    if (speed <= 65):
      return 0
    elif ((speed > 65) and (speed <= 85)):
      return 1
    else:
      return 2
  else:
    if (speed <= 60):
      return 0
    elif ((speed > 60) and (speed <= 80)):
      return 1
    else:
      return 2

def sorta_sum(a, b):
  sum = (a + b)
  if ((sum >= 10) and (sum < 20)) :
    return 20
  return sum

def alarm_clock(day, vacation):
  if vacation:
    if ((day > 0) and (day < 6)):
      return '10:00'
    else:
      return 'off'
  else: 
    if ((day > 0) and (day < 6)):
      return '7:00'
    else:
      return '10:00'

def love6(a, b):
  if ((a == 6) or (b == 6) or ((a + b) == 6) or (abs(a - b) == 6)):
    return True
  return False

def in1to10(n, outside_mode):
  if (outside_mode and ((n <= 1) or (n >= 10))):
    return True
  elif ((n >= 1) and (n <= 10)):
    return True
  return False

def near_ten(num):
  if (((num % 10) <= 2) or ((num % 10) >= 8)):
    return True
  return False
