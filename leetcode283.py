'''def moveZeroes(nums):
    x=[]
    y=[]
    for i in range(len(nums)):
        if nums[i]==0:
            x.append(nums[i])
        else:
            y.append(nums[i])
    z=y+x
    print(z)
nums=[0,1,0,3,12]
moveZeroes(nums)
'''
#leetcode version
def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        idx=0
        for i in range(len(nums)):
            if nums[i]!=0:
                 nums[idx]=nums[i]
                 idx+=1
        for i in range(idx,len(nums)):
            nums[i]=0
        return nums
nums=[0,1,0,3,12]
print(moveZeroes(nums))
