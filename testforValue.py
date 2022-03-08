#return true if value in array appears more than once
#return false if value appears only once
"""
class Solution(object):
    def findVal(self,nums):
        temp_val={}

        for i in range(0,len(nums)):
            if nums[i]in temp_val:
                return True
            else:
                temp_val[nums[i]]=i
        
        return False 

nums=[12,4,9,7,9,22]
solution=Solution()
print(solution.findVal(nums))
"""


#determine if element is present more than once
"""
class Solution:
    def containsDuplcate(self,nums):
        d=[]
        for num in nums:
            if num in d:
                return True
            else:
                d.append(num)
                #print(f"num {num} d[num] {d[num]} d{d}")
        print(d)
        return False



nums=[1,2,3,5]
solution=Solution()
print(solution.containsDuplcate(nums))

"""


#practice3
#given an array of values, return the third highest
'''
class Solution:
    def __init__(self, nums)-> None:
        self.nums=nums

    def thirdHighestEasy(self):
        self.nums.sort()
        return self.nums[-3]
    
    def thirdHighestHard(self):
        #accending sort algorithim
        l=len(self.nums)
        for i in range(0,l-1):
            for j in range(i+1,l):
                if self.nums[i]>self.nums[j]:
                    temp=self.nums[i]
                    self.nums[i]=self.nums[j]
                    self.nums[j]=temp
                else: 
                    continue
        #find 3rd value from last
        val_count=l-3
        i=0
        for i in range(0,l-1):
            if i==val_count:
                return self.nums[i]
                break
      
nums=[19,22,3,7,12,90,18,6,4,28,7]
solution=Solution(nums)
#print(solution.thirdHighestEasy())
print(solution.thirdHighestHard())

'''