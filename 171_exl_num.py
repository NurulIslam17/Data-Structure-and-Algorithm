def titleToNumber(s):
   res = 0
   multiply = 1
   for i in range(len(s) - 1, -1, -1):
      val = ord(s[i])-64
      res += val * multiply
      multiply *= 26
   return res


columnTitle = "AC"
print(titleToNumber(columnTitle))
