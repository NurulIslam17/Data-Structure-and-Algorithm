def twoSum(nums, target):
   l = 0
   r = len(nums) - 1
   while l < r:
      two_sum = nums[l] + nums[r]
      if two_sum < target:
         l += 1
      elif two_sum > target:
         r -= 1
      else:
         return [l + 1, r + 1]
   return []


nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))
