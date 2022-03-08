class Solution(object):
    def targetLocate(self,nums,target):
        high=len(nums)
        low=0
        
        for i in range(low,high):
            while high>=low:
                mid=(high+low)//2
                print(f"mid:{mid}")
                if nums[mid]==target:
                    return mid
                elif target>nums[mid]:
                    low=mid+1
                    print(f"new low: {low}")
                elif target < nums[mid]:
                    high=mid-1
                    print(f"new high: {high}")
                else:
                    return -1
        return -1


nums=[1,2,4,8,10,11,14]
target=14
solution=Solution()
print(solution.targetLocate(nums,target))


#binary search itterative
"""
def binary_searchI(nums,high,low,target):
    #print(nums,high,low,target)
    while high>low:
        for i in range(low,high):
            mid_index=(high+low)//2
            if target==nums[mid_index]:
                return mid_index
            elif target>nums[mid_index]:
                low=mid_index+1
            elif target<nums[mid_index]:
                high=mid_index-1
            else:
                return -1
  
    return -1


    target=13
nums=[-1,0,3,5,9,12]
print(binary_searchI(nums,len(nums)-1,0,target))

"""


"""
#binary search recursive
def binary_searchR(nums,target,high,low):
    if high>low:
        mid_index=(high+low)//2
        
        #test if nums[mid_index]== target
        if nums[mid_index]==target:
            return mid_index
        #test if target is larger than middle value
        elif target>nums[mid_index]:
           low=mid_index+1
           return binary_searchR(nums,target,high,low)
        elif target<nums[mid_index]:
            high=mid_index-1
            return binary_searchR(nums,target,high,low)
    else:
        return -1
    


target=5
nums=[-1,0,3,5,9,12]
print(binary_searchR(nums,target,len(nums),0))
"""