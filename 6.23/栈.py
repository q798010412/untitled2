class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.size = 0

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.size -= 1

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)
    def stack_size(self):
        return self.size
if __name__ == '__main__':
    stack=Stack()
    for i in range(10):
        stack.push(i)
    print(stack)
    for i in range(5):
        stack.pop()
    print(stack)
    print(stack.peek())
    print(stack.is_empty())
    print(stack.stack_size())