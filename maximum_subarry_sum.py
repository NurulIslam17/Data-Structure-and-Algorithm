def maximumSubarraySum(nums, k):
   i = 0
   j = 0
   sum, maxSum = 0, 0
   while j < len(nums):
      sum += nums[j]
      if j - i + 1 < k:
         j += 1
      elif j - i + 1 == k:
         maxSum = max(maxSum,sum)
         sum -= nums[i]
         i += 1
         j += 1
   return maxSum


nums = [2, 3, 1, 3, 7, 5, 5, 2]
k = 3
print(maximumSubarraySum(nums, k))
