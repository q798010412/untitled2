# 数组
# class Stack:
#     def __init__(self,limit=10):
#         self.stack=[]
#         self.size=0
#     def __str__(self):
#         return str(self.stack)
#     def push(self,data):
#         self.stack.append(data)
#         self.size+=1
#     def pop(self):
#         if self.stack:
#             self.stack.pop()
#             self.size-=1
#     def peek(self):
#         return self.stack[-1]
#     def is_empty(self):
#         return not bool(self.stack)
#     def stack_size(self):
#         return self.size
# if __name__ == '__main__':
#     n=Stack()
#     for i in range(10):
#         n.push(i)
#     print(n)
#     for i in range(6):
#         n.pop()
#     print(n)
#     print(n.peek())
#     print(n.is_empty())
#     print(n.stack_size())


# 链表
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node(%s)' % (self.data)


class LinkStack:
    def __init__(self, limit=10):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            self.top = self.top.next
        self.size -= 1

    def peek(self):
        return self.top

    def is_empty(self):
        return self.size is None

    def stack_size(self):
        return self.size

    def __repr__(self):
        cur = self.top
        str1 = ''
        while cur:
            str1 = str1 + 'Node(%s)-->' % (cur.data)
            cur = cur.next
        return str1 + 'END'


n = LinkStack()
n.push(1)
n.push(2)
n.push(3)
print(n)
n.pop()
print(n)
print(n.peek())
print(n.is_empty())
print(n.stack_size())
