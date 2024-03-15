def productExceptSelf(nums):
   answer = [1] * len(nums)
   pre = 1
   for i in range(len(nums)):
      answer[i] = pre
      pre *= nums[i]
   post = 1
   for i in range(len(nums) - 1, -1, -1):
      answer[i] *= post
      post *= nums[i]
   return answer


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
