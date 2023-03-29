def double_char(str):
  new = ''
  for i in str :
    new += (i + i)
  return (new)

def count_hi(str):
  target = 'hi'
  count = 0
  pos = 0
  while (pos <= (len(str) - 2)) :
    if (str[pos:(pos + 2)] == target) :
      count += 1
    pos += 1
  return (count)

def cat_dog(str):
  cats = 0
  dogs = 0
  for i in range(len(str) - 2) :
    if (str[i:(i + 3)] == 'cat') :
      cats += 1
    elif (str[i:(i + 3)] == 'dog') :
      dogs += 1
  return (cats == dogs)

def count_code(str):
  code = 0
  for i in range(len(str) - 3) :
    if ((str[i:(i + 2)] == 'co') and (str[(i + 3)] == 'e')) :
      code += 1
  return code

def end_other(a, b):
  if (len(a) > len(b)) :
    larger = a
    smaller = b
  else :
    larger = b
    smaller = a
  difference = (len(larger) - len(smaller))
  return (larger[difference:].lower() == smaller.lower())

def xyz_there(str):
  for i in range(len(str) - 2) :
    if ((str[i:(i + 3)] == 'xyz') and (str[(i - 1)] != '.')) :
      return True
  return False