class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node(%s)' % (self.data)


class LinkList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        if self.head is None:
            self.insert_head(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def append(self, i, data):
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            cur = self.head
            pre = cur
            j = 1
            while j < i:
                pre = cur
                cur = cur.next
                j += 1
            new_node = Node(data)
            pre.next = new_node
            new_node.next = cur
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
    def __repr__(self):
        curent = self.head
        curent_str = ''
        while curent:
            curent_str += '%s' % (curent) + '-->'
            curent = curent.next
        return curent_str + 'end'


a = LinkList()
a.insert_head(100)
a.insert_head(99)
a.insert_tail(55)
a.append(2, 200)
print(a)
a.del_tail()
a.del_head()
print(a)
