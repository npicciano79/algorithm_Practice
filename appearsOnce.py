#given array of ints, nums, return the value that appears only once

#solution with dictionary
"""
class Solution(object):
    def appearsOnce(self, nums):
        dict={}
       
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        
        for key, value in dict.items():
            if value==1:
                return key
        
        return None

nums=[1,3,4,5,5,4,3]
solution=Solution()
print(solution.appearsOnce(nums))
"""

#solution with array
class Solution(object):
    def appearsOnce(self, nums):
        no_Repeat=[]
        for num in nums:
            if num not in no_Repeat:
                no_Repeat.append(num)
            else:
                no_Repeat.remove(num)
        
        return no_Repeat


nums=[1,2,2]
solution=Solution()
print(solution.appearsOnce(nums))