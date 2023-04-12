#linked list merge sort 

class Node:

    def __init__(self,data,n=None,p=None):
        self.data=data
        self.next=n
        self.prev=p
    
    def __str__(self):
        return ('('+str(self.data)+')')

class LinkedList:
    def __init__(self,r=None):
        self.head=r
        self.size=0
    
    def add(self,d):
        new_node=Node(d,self.head)
        self.head=new_node
        self.size+=1

    def printList(self):
        this_node=self.head
        ll_array=[]
        while this_node is not None:
            ll_array.append(this_node.data)
            this_node=this_node.next
        
        return ll_array
    
    def mergeSortList(self,head):
        if not self.head or not self.head.next:
            return self.head
        
        left=self.head
        right=self.getMiddle(self.head)
        temp=right.next
        right.next=None
        right=temp

        left=self.mergeSortList(left)
        right=self.mergeSortList(right)

        return self.mergeLeftRight(left,right)


        
    def getMiddle(self,head):
        slow,fast=self.head,self.head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow

    def mergeLeftRight(self,left,right):
        dummy=tail=Node()
        while left and right:
            if left.data<right.data:
                tail.next=left
                left=left.next 
            else:
                tail.next=right
                right=right.next
            tail=tail.next 

        if left:
            tail.next=left
        if right:
            tail.next=right
        return dummy.next
    





linkedlist=LinkedList()
linkedlist.add(2)
linkedlist.add(1)
linkedlist.add(5)
linkedlist.add(9)
linkedlist.add(12)
linkedlist.add(7)
print(linkedlist.printList())
linkedlist.mergeSortList()