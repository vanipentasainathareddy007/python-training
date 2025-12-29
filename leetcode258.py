class Solution:
    def addDigits(self,num):
        while num>=10:
            sum=0
            while num>0:
                rem=num%10
                sum+=rem
                num=num//10
            num=sum
        return num

s=Solution()
print(s.addDigits(38))
