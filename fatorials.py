def factorials(n):
   if n == 1:
      return 1
   return n * factorials(n - 1)


if __name__ == "__main__":
   res = factorials(5)
   print(f"Factorials : {res}")
