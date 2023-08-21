import math

def isprimebad(n):
  c=1
  if n < 2:
    return False
  else:
    for i in range(2, int(math.sqrt(n))+1):
      if n%i == 0:
        c=0
        return False
    else:
        pass
    if c==1:
        return True
print(list(filter(isprimebad,range(1,1000))))

a=input()