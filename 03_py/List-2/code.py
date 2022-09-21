def count_evens(nums):
  evens = 0
  for i in nums:
    if ((i % 2) == 0):
      evens += 1
  return evens

def big_diff(nums):
  nums.sort()
  return (nums[-1] - nums[0])

def centered_average(nums):
  nums.sort()
  total = 0
  for i in range(len(nums) - 1) :
    if (i != 0) :
      total += nums[i]
  return (total / (len(nums) - 2))

def sum13(nums):
  sum = 0
  for i in range(len(nums)) :
    if ((nums[i] != 13) and (nums[(i - 1)] != 13)) :
      sum += nums[i]
    elif ((i == 0) and (nums[0] != 13)) :
      sum += nums[i]
  return sum

def sum67(nums):
  sum = 0
  ignore = False
  for i in nums :
    if (i == 6) :
      ignore = True
    elif not ignore :
      sum += i
    elif (i == 7) :
      ignore = False
  return sum

def has22(nums):
  for i in range(len(nums) - 1) :
    if ((nums[i] == 2) and (nums[(i + 1)] == 2)) :
      return True
  return False
