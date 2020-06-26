class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node(%s)' % (self.data)


class LinkedStack:
    def __init__(self, limit=10):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next=self.top
        self.top=node
    def pop(self):
        if self.top:
            self.top = self.top.next
            return self.top

    def peek(self):
        return self.top

    def is_empty(self):
        return self.top is None

    def __repr__(self):
        cur = self.top
        str1 = ''
        while cur:
            str1 = str1 + 'Node(%s)-->' % (cur.data)
            cur = cur.next
        return str1 + 'END'


a = LinkedStack()
a.push(1)
a.push(2)
a.push(100)
a.push(500)
a.pop()
print(a.peek())
print(a)
print(a.is_empty())
