n=int(input())

def sq(n):
    for i in range(1, n+1):
        yield i**2


for square in sq(n):
    print(square) 
