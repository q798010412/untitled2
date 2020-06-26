class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur

    def insert(self, index, data):
        new_node = Node(data)
        if index < 1 or index > self.size+1:
            raise Exception('索引越界')
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 1:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            pre = self.get(index-1)
            new_node.next = pre.next
            pre.next = new_node
        self.size += 1
    def remove(self,index):
        if index<0 or index>=self.size:
            raise Exception('索引越界')
        elif index==0:
            self.head=self.head.next
        elif index==self.size-1:
            removed_node=self.get(index-1)
            removed_node.next=None
            self.tail=removed_node
        else:
            pre=self.get(index-1)
            removed_node=self.get(index)
            pre.next=removed_node.next
        self.size-=1
    def reserve(self):
        pre=None
        cur=self.head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        self.head=pre
    def __repr__(self):
        cur = self.head
        str1 = ''
        while cur:
            str1 = str1 + 'Node(%s)-->' % (cur.data)
            cur = cur.next
        return str1 + 'END'


n = LinkList()
n.insert(1,0)
n.insert(1,1)
n.insert(2,2)
n.insert(3,3)
print(n)
# n.remove(1)
# n.remove(0)
# print(n)
n.reserve()
print(n)