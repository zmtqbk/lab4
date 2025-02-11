n=int(input())

def divible(n):
    for i in range(0, n+1):
        if i%3==0 and i%4==0:
            yield i

for divnum in divible(n):
    print(divnum)