#412fizzbuzz - given an integer, return string array where
#if i mod 3, "Fizz"
#if i mod 5, Buzz
#if i mod 3 and 5, FizzBuzz
#Else i

"""
class Solution(object):
    def fizzBuzz(self,n):
        answer=[]
        for i in range(1,n+1):
            word=''
            if i%3==0:
                word+='Fizz'
            if i%5==0:
                word+='Buzz'
            if word=='':
                word=str(i)
            
            answer.append(word)
        return answer

n=15
solution=Solution()
print(solution.fizzBuzz(n))
"""

#solution using dictionary
class Solution(object):
    def fizzBuzz(self,n):
        dictFizzBuzz={3:'Fizz',5:'Buzz'}
        answer=[]
        for i in range(1,n+1):
            ans_str=''
            for key in dictFizzBuzz.keys():
                if i%key==0:
                    ans_str+=dictFizzBuzz[key]
                
            if ans_str=='':
                ans_str=str(i)

            answer.append(ans_str)
        return answer


n=20
solution=Solution()
print(solution.fizzBuzz(n))
                









#& C:/Users/npicc/Documents/python/python.exe c:/Users/npicc/Documents/Coding/projects/lc_practice/fizzbuzz.py