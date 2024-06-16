from typing import List

class ListNode:
    def __init__(self,data):
        self.data = data 
        self.next =None

class LinkedList:
    def __init__(self):
        self.head = None
    def add(self,data):
        if not self.head:
            self.head=ListNode(data)
        else :
            current =self.head
            while current.next:
                current=current.next 
            current.next=ListNode(data)

def double_it(A:LinkedList)->List:
    current = A.head 
    string_list = []
    output = []
    while current:
        string_list.append(str(current.data))
        current = current.next 
    concated_str = ''.join(string_list)
    integer= int(concated_str)
    integer = integer*2 
    concated_str=str(integer)
    for item in concated_str:
        output.append(int(item))
        
    return output 
        

ll = LinkedList()
ll.add(1)
ll.add(2)
result = double_it(ll)
print (result)




    

