def OperationChoices(c,a,b):
  if c ==1:
    return (a+b)
  elif c==2:
    return (a-b)
  elif c==3:
    return (a*b)
  else:
    return (a//b)
c,a,b=map(int,input().split())
print(OperationChoices(c,a,b))
