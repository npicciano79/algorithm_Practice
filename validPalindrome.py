
"""
#125 valid palindrome - determine if a string is a valid palindrome
class Solution:
    def __init__(self,s) -> None:
        self.s=s
        
        

    def isPalindrome(self):
        
            newS=s.lower()
            vals={',',':',' ','.'}
            foward=[]
            for i in newS:
                if i not in vals:
                    foward.append(i)  
            
            result=True
            l=len(foward)-1
            while l>l//2:
                for j in foward:
                    if j!=foward[l]:
                        return False
                    else:
                        l-=1
            return True

s=".b"
solution=Solution(s)
print(solution.isPalindrome())
"""
#125 valid palindrome - solution using isalnum() function
"""
class Solution:
    def __init__(self,s) -> None:
        self.s=s

    def isPalindrome(self):
        if not s:
            return True
        newVal=''
        for i in s:
            if i.isalnum()==True:
                newVal+=i.lower()
        if newVal==newVal[::-1]:
            return True
        else:
            return False   
s="a2sbcbsa"
solution=Solution(s)
print(solution.isPalindrome())
"""










#C:/Users/npicc/Documents/python/python.exe c:/Users/npicc/Documents/Coding/projects/lc_practice/practice3.py