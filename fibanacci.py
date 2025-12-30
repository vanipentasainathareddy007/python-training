'''def fib(n):
    a=0
    b=1 
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b 
        a=b 
        b=c 
        print(c)
n=int(input())
fib(n)'''
#recursion
def fib(n):
    if n==0 or n==1 :
        return n
    return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
  