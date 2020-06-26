from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def append(self, data):
        if self.head is None:
            self.insert_head(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert(self, i, data):
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            new_node = Node(data)
            cur = self.head
            pre = cur
            j = 1
            while j < i:
                pre = cur
                cur = cur.next
            pre.next = new_node
            new_node.next = cur

    def linklist(self, obj: List):
        new_node = Node(obj[0])
        self.head = new_node
        cur = new_node
        for i in obj[1:]:
            cur.next = Node(i)
            cur = cur.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def del_head(self):
        if self.head is None:
            print('空链表')
        else:
            self.head = self.head.next

    def del_tail(self):
        if self.head is None:
            print('空链表')
        else:
            cur = self.head
            pre = cur
            while cur.next:
                pre = cur
                cur = cur.next
            pre.next = None
            return cur.data

    def __repr__(self):
        cur = self.head
        str_1 = ''
        while cur:
            str_1 = str_1 + 'Node(%s)-->' % (cur.data)
            cur = cur.next
        return str_1 + 'END'


a = LinkList()

a.linklist([1, 23, 4, 5])
print(a)
a.del_tail()
print(a)
