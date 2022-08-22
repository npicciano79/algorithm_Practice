#create fibbonacci sequence for a given set of values

#Returns entire fibbonacci sequence for a given value
"""
class Solution(object):
    def fibbonacci(self,value):
        sequence=[]
        prevVal=0
        currVal=1
        count=0
        while count<=value:
            sequence.append(currVal)
            currVal=currVal+prevVal
            prevVal=sequence[count]
            count+=1
        

        return sequence     

value=12
solution=Solution()
print(solution.fibbonacci(value))
"""

#returns value in the position of a fibbonacci sequence

"""
class Solution(object):
    def fibbonacci(self, value):
        prevVal=0
        currVal=1
        count=1
        while count<value:
            tempVal=currVal
            currVal=currVal+prevVal
            prevVal=tempVal
            count+=1
        
        return currVal
        
value=3
solution=Solution()
print(solution.fibbonacci(value))
"""


class Solution(object):
    def fib(self,n):
        if n<=2:
            return n
        else:
            return self.fib(n-2)+self.fib(n-1)

solution=Solution()
print(solution.fib(5))