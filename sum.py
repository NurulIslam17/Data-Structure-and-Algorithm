def solve(n):
   if n == 1:
      return 1
   return n + solve(n - 1)


if __name__ == '__main__':
   res = solve(5)
   print(res)
