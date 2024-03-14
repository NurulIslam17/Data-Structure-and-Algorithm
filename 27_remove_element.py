def removeElement(nums, val):
   i = j = 0
   while i < len(nums):
      if nums[i] != val:
         nums[j] = nums[i]
         j += 1
      i += 1
   return j


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
res = removeElement(nums, val)
print(res)
