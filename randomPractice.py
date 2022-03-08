#C:/Users/npicc/Documents/python/python.exe pract2.py
"""
class Solutions(object):
    def searchInsert(self,nums,target):
        
        l=len(nums)
        if target<nums[0]:
            return 0
        else:
            for i in range(l-1,-1,-1):
                if target==nums[i]:
                    return i
                    break
                elif target>nums[i]:
                    return i+1
                    break
        
        l=len(nums)
        for i in range(l-1,-1,-1):
            if nums[i]<target:
                break
            else:
                l-=1
        return l   

nums=[1]
solution=Solutions()
print(solution.searchInsert(nums,2))
"""

"""
class Solution(object):
    def lengthLastWord(self,s):
        count=0
        for i in s.split():
            val=i
        
        return val

s="Hello World "
solution=Solution()
print(solution.lengthLastWord(s))
"""
class Solution(object):
    def maxProfit(self,prices):
        l=len(prices)
        dif = prices[1]-prices[0]
        for i in range(0,l):
            for j in range(i+1,l):
                t_dif=prices[j]-prices[i]
                #input(f" tdif:{t_dif} i: {i} j:{j}")
                if t_dif>dif:
                    dif=t_dif
                    #input(f"dif: {dif}")
                    start=i+1
                    stop=j+1

        if dif<0:
            return 0
        else:
            return stop

        
 

prices=[7,6,4,3,1]
solution=Solution()
print(solution.maxProfit(prices))





"""

class Cpractice:

    def __init__(self,first_val,second_val,) -> None:
        self.first_val=first_val
        self.second_val=second_val  
    
    def opps(self):
        return self.first_val+self.second_val

    def compare(self):
        if self.first_val<=self.second_val:
            return self.second_val
        else:
            return self.first_val

        
cpractice=Cpractice(93,100)

print(cpractice.second_val)
print(cpractice.first_val)
print(cpractice.opps())
print(cpractice.compare())
"""

import random

"""
def loop(n):
    for i in range(n):
        print(f"i: {i}")

def arr(k,l):
    #for i in k:
        #print(f"i: {i}")
    print(k[1:])


#n=4
#loop(n)

k=[1,2,3,4,5,6]
l=3
arr(k,l)

cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra}  
"""

words = {"ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam" ,"cobra"} 

print(words[1])