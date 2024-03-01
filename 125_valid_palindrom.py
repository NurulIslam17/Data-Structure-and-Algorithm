def isPalindrome(s):
   res = False
   test_str = ''.join(letter for letter in s if letter.isalnum())
   temp_str = test_str
   rev_str = test_str[::-1]

   if rev_str.lower() == temp_str.lower():
      res = True
   return res


# s = "A man, a plan, a canal: Panama"
s = "race a car"
print(isPalindrome(s))
