def singleNumber(nums):
   res = 0
   for i in range(len(nums)):
      res = res ^ nums[i]
   return res


nums = [1, 2, 3, 4, 4, 2, 3]
print(singleNumber(nums))
