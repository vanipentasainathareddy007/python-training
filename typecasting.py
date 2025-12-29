def kk(nums):
    s=""
    k=[]
    for num in nums:
        s+=str(num)
    i=str(int(s)+1)
    for ch in i:
        k.append(int(ch))
    print(k)
nums=[9,9,9]
kk(nums)