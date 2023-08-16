def mangoDistribution(input1, input2):
  from math import factorial
   k = input1
   n = input2
   result = factorial(n+k-1)// (factorial(k)) * (factorial(n-1))
   return result
input1= int(input())
input2= int(input())
print(mangoDistribution(input1,input2))



















  
