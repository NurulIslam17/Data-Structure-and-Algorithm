def firstNegative(nums, k):
   negative = []
   i, j = 0, 0
   while j < len(nums):
      if j - i + 1 < k:
         j += 1
      elif j - i + 1 == k:
         for n in range(i, j + 1):
            if nums[n] < 0:
               negative.append(nums[n])
               break

         j += 1
         i += 1
   return negative


nums = [2, -1, 1, 1, -2, -3, 4, -4]
k = 3
print(firstNegative(nums, k))
