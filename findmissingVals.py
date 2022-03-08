#268 missing number
#given array nums containing vals[0,n] return only the number in the range that is missing

"""
class Solution:
    def missingNumber(self,nums):
        count=0
        while count<=len(nums)-1:
            if count not in nums:
                return count
            else:
                count+=1
        return count
            
        

nums=[0]
solution=Solution()
print(solution.missingNumber(nums))
"""

#488 find all numbers disappeared in an array
#given array nums of n integers where nums[i] is in the range [1,n]
#return an array of all the integers in range [1,n] that do not appear in nums
"""
class Solution:
    def findDisappearedNumber(self,nums):
        count=1
        l=len(nums)-1
        answer=[]
        while count<l:
            if count not in nums:
                answer.append(count)
            else:
                count+=1
        return answer

nums=[4,3,2,7,8,2,3,1]
solution=Solution()
solution.findDisappearedNumber(nums)


"""
