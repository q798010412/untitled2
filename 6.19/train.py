from typing import List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return 'Node(%s)'%(self.data)

class LinkList:
    def __init__(self):
        self.head=None
    def insert_head(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
        self.head=new_node
    def insert_tail(self,data):
        if self.head is None:
            self.insert_head(data)
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=Node(data)

    def insert_midel(self,i,data):
        if self.head is None or i==1:
            self.insert_head(data)
        else:
            new_node=Node(data)
            curr=self.head
            prev=curr
            j=1
            while j<i:
                prev=curr
                curr=curr.next
                j+=1
            prev.next=new_node
            new_node.next=curr
    def linklist(self,obj:List):
        new_node=Node(obj[0])
        self.head=new_node
        cur=self.head
        for i in obj[1:]:
            cur.next=Node(i)
            cur=cur.next

    def print_list(self):
        current=self.head
        while current:

            print(current.data)
            current=current.next

    def __repr__(self):
        cur=self.head
        str_1=''
        while cur:
            str_1=str_1+'Node(%s)-->'%(cur.data)
            cur=cur.next
        return str_1+"END"
a=LinkList()
# a.insert_head(3)
# a.insert_head(1)
# a.insert_tail(2)
# a.insert_midel(3,4)
a.linklist([1,2,3,4,5])
a.linklist([1])
a.print_list()
print('-------')
print(a)