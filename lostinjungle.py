def lostinjungle(M):
  res = dict()
  for i in range(1, M+1):
    n = i
    count = 0
    while n>1:
      if n % 2 == 0:
        n // 2
        count+=1
      else:
        n = (3*n)+1
        count+=1
    res[count]=i
  print(res)
M = int(input())
print(lostinjungle(M))
