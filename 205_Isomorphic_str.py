def isIsomorphic(s, t):
   if len(s) != len(t):
      return False
   hashS, hashT = {}, {}

   for c1, c2 in zip(s, t):
      if ((c1 in hashS and hashS[c1] != c2) or
           (c2 in hashT and hashT[c2] != c1)):
         return False
      hashS[c1] = c2
      hashT[c2] = c1
   return True


s = "eguu"
t = "adgg"
print(isIsomorphic(s, t))
