def productExceptSelf(nums):
   answer = []
   for i in range(len(nums)):
      mult = 1
      for j in range(len(nums)):
         if i != j:
            mult *= nums[j]
      answer.append(mult)
   return answer


nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
