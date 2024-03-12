def maxVal(i, j, nums):
   maxVal = 0
   for n in range(i, j + 1):
      if nums[n] > maxVal:
         maxVal = nums[n]
   return maxVal


def maximumValOfSubarray(nums, k):
   max_list = []
   i, j = 0, 0
   while j < len(nums):
      if j - i + 1 < k:
         j += 1
      elif j - i + 1 == k:
         val = maxVal(i, j, nums)
         max_list.append(val)
         i += 1
         j += 1
   return max_list


nums = [4, 5, 6, 8, 1, 9, 2]
k = 4
print(maximumValOfSubarray(nums, k))
