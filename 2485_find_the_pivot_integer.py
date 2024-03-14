def pivotInteger(n):
   value = []
   total_sum = 0
   for i in range(1, n + 1):
      total_sum += i
      value.append(i)
   left_sum = 0
   for i in range(len(value)):
      right_sum = total_sum - left_sum - value[i]
      if left_sum == right_sum:
         return value[i]
      left_sum += value[i]
   return -1


n = 8
print(pivotInteger(n))
