n=int(input())

def even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i

for evennum in even(n):
    print(evennum, end=", ") 