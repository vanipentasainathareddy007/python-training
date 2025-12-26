def cupcakes(n,a):
    sum=0
    for i in range(n):
        if a[i]>=5:
            sum+=a[i]
    print(sum)
n=5
a=[1,2,5,8,3,7]
cupcakes(n,a)
