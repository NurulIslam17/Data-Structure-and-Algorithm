def fibo(n, dp):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   elif dp[n] != -1:
      return dp[n]
   else:
      dp[n] = fibo(n - 1, dp) + fibo(n - 2, dp)
      return dp[n]


n = int(input('Enter Number : '))
dp = [-1] * (n + 1)
print(fibo(n, dp))
