"""
class Solution:
    def reverseArray(self,arr):
        i=0
        j=len(arr)-1
        #print(arr[j])
      
        while i<j:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
            j-=1
            i+=1
        
        print(arr)
                
arr=['1','2','3','4','5','6']
solution=Solution()
solution.reverseArray(arr)
"""

#in-place sort of array
"""
class PostionSort:
    def quicksort(arr,start,stop):
        if start < stop:
            pivotindex=partitionrand()
        
        
        return arr

    def partitionrand(arr,start,stop):
"""

"""
class Arraysort:
    def __init__(self,arr) -> None:
        self.arr=arr
    
    def AscendSort(self):
        l=len(self.arr)
        
        for i in range(0,l-1):
            for j in range(i+1,l):
                if self.arr[i]>self.arr[j]:
                    temp=self.arr[j]
                    self.arr[j]=self.arr[i]
                    self.arr[i]=temp
                    input(f"sort-temp: {temp} j {j} value: {self.arr[j]} i: {i} value: {self.arr[i]}")
                    input(arr)
                else:
                    input(f"not sort-j: {j} value {self.arr[j]} i {i} value: {self.arr[i]} ")
                    input(arr)
        return arr
        
        

arr=[2,1,5,3]
arraysort=Arraysort(arr)
print(arraysort.AscendSort())
"""

