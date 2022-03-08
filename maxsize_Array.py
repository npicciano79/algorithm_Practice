#given array of integers size n, 
#calculate the max sum of k consecutive elements in the array
#bruit force

import sys

"""
INT_MIN=-sys.maxsize-1

def maxSum(arr,n,k):
    #initalize result
    max_sum=INT_MIN
    #consider all blocks beginning with i
    for i in range(n-k+1):
        current_sum=0
        for j in range(k):
            current_sum=current_sum+arr[i+j]     #adds next value
        
        max_sum=max(current_sum,max_sum)
    return max_sum
"""

#sliding window technique

def maxSum(arr,k):
    #length of array
    n=len(arr)
    print(f"length: {n}")
    #n must be greater than k
    if n<k:
        print("invalid")
        return -1

    #compute sum of first window size of k
    window_sum=sum(arr[:k])
    print(f"window sum: {window_sum}")

    #first sum available
    max_sum= window_sum

    #compute first sums of remaining windows by removing
    #first element of previous window and adding last element 
    #of the current window
    for i in range(n-k):
        print(f"i:{i}")
        window_sum=window_sum-arr[i]+arr[i+k]
        print(f"window sum: {window_sum}")
        max_sum=max(window_sum,max_sum)
        print(f"max sum: {max_sum}")
    
    return max_sum








arr=[1,4,2,10,2,3,1,0,20]
k=4
print(maxSum(arr,k))

