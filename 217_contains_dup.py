def containsDuplicate(nums):
   unique = set()
   for i in nums:
      if i in unique:
         return True
      else:
         unique.add(i)
   return False


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
