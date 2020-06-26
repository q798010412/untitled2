class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        str1 = 'Node(%s)' % (self.data)
        return str1


class LinkQueue:
    def __init__(self):
        self.front = None
        self.tail = None
        self.size = 0

    def put(self, data):
        node = Node(data)
        if self.front is None:
            self.front = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop(self):
        if self.front is None:
            raise Exception('queue is empty')
        else:
            self.front = self.front.next
        self.size -= 1

    def get(self, index):
        if self.front is None:
            raise Exception('queue is empty')
        elif index<1 or index>self.size:
            raise Exception('index out of range')
        else:
            cur=self.front
            for i in range(1,index):
                cur=cur.next
            return cur

    def __repr__(self):
        cur = self.front
        str_cur=''
        while cur:
            str_cur = str_cur + 'Node(%s)<--' % (cur.data)
            cur=cur.next
        return str_cur+'END'
n=LinkQueue()
n.put(1)
n.put(2)
n.put(3)
print(n)
print(n.get(1))
n.pop()
print(n)