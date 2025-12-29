
def majorityElement(nums):
        c=0
        can=0
        for num in nums:
            if c==0:
                can=num
                c+=1
            elif can==num:
                c+=1
            else:
                c-=1
        return can
nums=[2,2,1,1,1,2,2,2]
print(majorityElement(nums))
        