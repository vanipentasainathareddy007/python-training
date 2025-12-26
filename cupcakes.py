'''x="madam"
l=0
r=len(x)-1
while l<r:
    if x[l]==x[r]:
        l+=-1
        r-=-1
        print("palindrome")
    else:
        print("not a palindrome")'''
def cupcakes(n,a):
    sum=0
    for i in range(n):
        if a[i]>=5:
            sum+=a[i]
    print(sum)
n=5
a=[1,2,5,8,3,7]
cupcakes(n,a)