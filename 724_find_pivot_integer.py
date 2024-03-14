def pivotInteger(nums):
   total_sum = sum(nums)
   left_sum = 0
   for i in range(len(nums)):
      right_sum = total_sum - left_sum - nums[i]
      if left_sum == right_sum:
         return i
      left_sum += nums[i]
   return 0


nums = [1, 7, 3, 6, 5, 6]
print(pivotInteger(nums))
