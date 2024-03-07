def isHappy(n):
   visited = set()

   while n not in visited:
      visited.add(n)
      n = squareOfNum(n)
      if n == 1:
         return True
   return False


def squareOfNum(n):
   square_sum = 0
   while n:
      digit = n % 10
      digit = digit ** 2
      square_sum += digit
      n = n // 10
   return square_sum


n = 19
print(isHappy(n))
