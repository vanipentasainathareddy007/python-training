'''def fac(n):
    f=1 
    for i in range(1,n+1):
        f*=i
    print(f)
fac(5)'''
#recursion
def fact(n):
    if n==0 or n==1:
        return n
    return n*fact(n-1)
print(fact(6))