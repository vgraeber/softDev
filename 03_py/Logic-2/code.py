def make_bricks(small, big, goal):
  if (goal == 0):
    return True
  else:
    if (goal > (small + (big * 5))):
      return False
    elif (small < (goal % 5)):
      return False
    else:
      r = goal % 5
      small -= r
      goal -= r
      if (((big * 5) + small) >= goal):
        return True
      else:
        return False

def lone_sum(a, b, c):
  a2 = a
  b2 = b
  c2 = c
  if (a == b == c) 
    a2 = 0
    b2 = 0
    c2 = 0
  elif (a == b):
    a2 = 0
    b2 = 0
  elif (a == c) 
    a2 = 0
    c2 = 0
  elif (b == c) 
    b2 = 0
    c2 = 0
  return (a2 + b2 + c2)

def lucky_sum(a, b, c) 
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
  if ((num % 10) >= 5):
    num = num + (10 - (num % 10))
  else:
    num = num - (num % 10)
  return num

def round_sum(a, b, c):
  return (round10(a) + round10(b) + round10(c))

def close_far(a, b, c):
  if ((abs(a - b) <= 1) or (abs(a - c) <= 1)):
    if ((abs(b - a) >= 2) and (abs(b - c) >= 2)):
      return True
    elif ((abs(c - a) >= 2) and (abs(c - b) >= 2)):
      return True
    else:
      return False
  else:
    return False

def make_chocolate(small, big, goal):
  if ((small + (big * 5)) < goal):
    return -1
  elif ((big * 5) > goal):
    dif = (big * 5) - goal
    if ((dif % 5) != 0):
      dif += 5 - (dif % 5)
    big -= (dif / 5)
    if ((small + (big * 5)) < goal):
      return -1
    else:
      goal -= big * 5
      return goal
  else:
    goal -= big * 5
    return goal
