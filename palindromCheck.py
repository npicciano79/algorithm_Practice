#palindrome test
#if value if palindrome, return true, else return false
from string import ascii_lowercase,ascii_uppercase



class Solution(object):
    def palindromeCheck(self, word):
        specialChar={1:',',2:".",3:"!",4:" "}
        wordArray=[]
        for i in range(0,len(word)):
            if word[i] not in specialChar.values():
                wordArray.append(word[i].lower())

        high=len(wordArray)-1
        low=0

        while high>low:
            if wordArray[low]!=wordArray[high]:
                return [False,wordArray]
            else:
                high-=1
                low+=1
        return [True,wordArray]
        


word='ZZZZ car, a man, a maracaz.'
solution=Solution()
print(solution.palindromeCheck(word))

