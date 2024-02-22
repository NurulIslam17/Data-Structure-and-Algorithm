def fibonacci(n):
   # it is to dangerous for large numbers
   # not good for health
   if n <= 2:
      return 1
   return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
   res = fibonacci(1)
   print(res)
