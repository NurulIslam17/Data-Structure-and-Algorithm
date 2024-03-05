def majorityElement(nums):
   counts = {}
   for num in nums:
      if num in counts:
         counts[num] += 1
      else:
         counts[num] = 1

   max_count = 0
   majority_element = None
   for num, count in counts.items():
      if count > max_count:
         max_count = count
         majority_element = num

   return majority_element


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
