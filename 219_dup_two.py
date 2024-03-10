def containsNearbyDuplicate(nums, k):
   windows = set()
   l = 0
   for r in range(len(nums)):
      if r - l > k:
         windows.remove(nums[l])
         l += 1
      if nums[r] in windows:
         return True
      windows.add(nums[r])
   return False


nums = [1, 0, 1, 1]
k = 2
print(containsNearbyDuplicate(nums, k))
