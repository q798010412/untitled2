class Array():
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        if self.size >= len(self.array):
            Array.addcapacity(self)
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.size += 1
        self.array[index] = element
        Array.output(self)

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    def output(self):
        for i in range(self.size):
            print(self.array[i], "->", end='')
        print()

    def remove(self, delelement):
        for i in range(self.size):
            if self.array[i] == delelement:
                for j in range(i, self.size):
                    self.array[j] = self.array[j + 1]
                self.size -= 1
        Array.output(self)


test = Array(3)
test.insert(0, 0)
test.insert(1, 1)
test.insert(2, 2)
test.insert(1, 30)
test.remove(2)




