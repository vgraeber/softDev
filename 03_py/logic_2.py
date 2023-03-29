def make_bricks(small, big, goal):
  if (goal > (small + (big * 5))):
    return False
  elif (small < (goal % 5)):
    return False
  return True

def lone_sum(a, b, c):
  if (a == b == c):
    a = 0
    b = 0
    c = 0
  elif (a == b):
    a = 0
    b = 0
  elif (a == c):
    a = 0
    c = 0
  elif (b == c):
    b = 0
    c = 0
  return (a + b + c)

def lucky_sum(a, b, c): 
  if (a == 13):
    return 0
  elif (b == 13):
    return a
  elif (c == 13):
    return (a + b)
  return (a + b + c)

def fix_teen(n):
  if ((n == 15) or (n ==16)):
    return n
  elif ((n >= 13) and (n <= 19)):
    return 0
  else:
    return n

def no_teen_sum(a, b, c):
  return (fix_teen(a) + fix_teen(b) + fix_teen(c))

def round10(num):
  return int(round(num, -1))

def round_sum(a, b, c):
  return (round10(a) + round10(b) + round10(c))

def close_far(a, b, c):
  if ((abs(a - b) <= 1) or (abs(a - c) <= 1)):
    if ((abs(b - a) >= 2) and (abs(b - c) >= 2)):
      return True
    elif ((abs(c - a) >= 2) and (abs(c - b) >= 2)):
      return True
    return False
  return False

def make_chocolate(small, big, goal):
  if (goal > (small + (big * 5))):
    return -1
  elif (small < (goal % 5)):
    return -1
  elif ((big * 5) > goal):
    dif = (big - (goal / 5))
    big -= dif
    goal -= (big * 5)
    return goal
  else:
    goal -= big * 5
    return goal