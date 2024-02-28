def generate(numRows):
   res = [[1]]
   for i in range(numRows - 1):
      temp = [0] + res[-1] + [0]
      new_row = []
      for j in range(len(res[-1]) + 1):
         new_row.append(temp[j] + temp[j + 1])
      res.append(new_row)
   return res


print(generate(6))
