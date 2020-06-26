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

    def insert_tali(self,data):
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

    def delete(self,i):
        if self.head is None:
            print('空链表')
        elif i==1:
            self.del_head()
        else:
            cur=self.head
            pre=cur
            j=1
            while j<i:
                pre=cur
                cur=cur.next
                j+=1
            pre.next=cur.next
    def linklist(self,obj):
        self.head=Node(obj[0])
        cur=self.head
        for i in obj[1:]:
            cur.next=Node(i)
            cur=cur.next

    def __repr__(self):
        cur=self.head
        str_1=''
        while cur:
            str_1=str_1+'Node(%s)-->'%(cur.data)
            cur=cur.next
        return str_1+'END'
n=LinkList()
n.insert_head(1)
n.insert_head(5)
n.insert_tali(6)
n.insert(1,100)
print(n)
n.del_tail()
n.del_head()
n.delete(2)
print(n)
n.linklist([1,2,3,4,5,6])
print(n)