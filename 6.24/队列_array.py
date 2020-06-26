class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.size = 0

    def __repr__(self):
        str1 = '<' + str(self.queue)[1:-1] + '>'
        return str1

    def put(self, data):
        self.queue.append(data)
        self.size += 1

    def get(self):
        dequeue = self.queue[self.front]
        self.size -= 1
        self.queue = self.queue[1:]
        return dequeue


n = Queue()
n.put(1)
n.put(2)
n.put(3)
n.get()
print(n)
