class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

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
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=Node(data)
    def insert(self,i,data):
        if self.head is None or i==1:
            self.insert_head(data)
        else:
            cur=self.head
            pre=cur
            j=1
            while j<i:
                pre=cur
                cur=cur.next
                j+=1
            new_node=Node(data)
            pre.next=new_node
            new_node.next=cur
    def del_head(self):
        if self.head is None:
            print('空链表')
        else:
            self.head=self.head.next
    def del_tail(self):
        if self.head is None:
            print('空链表')
        else:
            cur=self.head
            while cur.next.next:
                cur=cur.next
            cur.next=None
    def linklist(self,obj):
        self.head=Node(obj[0])
        cur=self.head
        for i in obj[1:]:
            cur.next=Node(i)
            cur=cur.next
    def __repr__(self):
        cur=self.head
        str1=''
        while cur:
            str1=str1+'Node(%s)-->'%(cur.data)
            cur=cur.next
        return str1+'END'

a=LinkList()
a.insert_head(1)
a.insert_head(2)
a.insert_tail(5)
a.insert(1,100)
print(a)
a.del_head()
a.del_tail()
print(a)
a.linklist([1,2,3,4,5])
print(a)