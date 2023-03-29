def first_last6(nums):
  if ((nums[0] == 6) or (nums[-1] == 6)):
    return True
  else:
    return False

def same_first_last(nums):
  if (len(nums) < 1):
    return False
  elif (nums[0] == nums[-1]):
    return True
  else:
    return False

def make_pi():
  return ([3, 1, 4])

def common_end(a, b):
  if ((a[0] == b[0]) or (a[-1] == b[-1])):
    return True
  else:
    return False

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  newArray = nums[1:]
  newArray.append(nums[0])
  return newArray

def reverse3(nums):
  nums.reverse()
  return nums

def max_end3(nums):
  if (nums[0] > nums[-1]):
    new = [nums[0]] * len(nums)
  else:
    new = [nums[-1]] * len(nums)
  return new

def sum2(nums):
  s = sum(nums[:2])
  return s

def middle_way(a, b):
  new = [a[1], b[1]]
  return new

def make_ends(nums):
  new = [nums[0], nums[-1]]
  return new

def has23(nums):
  for i in nums:
    if ((i == 2) or (i == 3)):
      return True
  return False