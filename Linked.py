class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        if self.head == None:
            self.head=Node(data,None)
        else:
            c= self.head
            while c.next:
                c=c.next
            c.next = Node(data,None)

    def print(self):
        d = self.head
        while d:
            print(d.data) 
            d = d.next

list=linklist()
list.append(5)
list.append(6)
list.append(9)
list.append(4)
list.append(3)           
list.print()
list1=linklist()
list1.append(55)
list1.print()

