import math

n=int(input())

len=int(input())

area=(n/4)*(len**2)*(1/math.tan(math.pi/n))
print(area)