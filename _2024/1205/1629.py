import sys
A,B,C = map(int,sys.stdin.readline().split())

def multiply (a,n):
    if n == 1:
        return a%C
    else:
        tmp = multiply(a,n//2)
        if n%2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * a) %C
        
print(multiply(A,B))