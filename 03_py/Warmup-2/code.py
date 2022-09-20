def string_times(str, n):
  output = (str * n)
  return output

def front_times(str, n):
  output = (str[0:3] * n)
  return output

def string_bits(str):
  output = ''
  for i in range(len(str)):
    if ((i % 2) == 0):
      output += str[i]
  return output

def string_splosion(str):
  output = ''
  for i in range(len(str)):
    output += str[0:(i + 1)]
  return output

def last2(str):
  endpart = str[-2:]
  times = 0
  for i in range(len(str) - 2):
    if (str[i:(i + 2)] == endpart):
      times += 1
  return times

def array_count9(nums):
  numNines = 0
  for i in nums:
    if (i == 9):
      numNines += 1
  return numNines

def array_front9(nums):
  first = nums[0:4]
  for i in first:
    if (i == 9):
      return True
  return False

def array123(nums):
  target = [1, 2, 3]
  present = False
  for i in range(len(nums) - 2):
    if (nums[i:(i + 3)] == target):
      return True
  return False

def string_match(a, b):
  if (len(a) < len(b)):
    lesser = len(a)
  else:
    lesser = len(b)
  matches = 0
  for i in range(lesser - 1):
    if (a[i:(i + 2)] == b[i:(i + 2)]):
      matches += 1
  return matches
