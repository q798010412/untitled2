class Array():
    def __init__(self,capacity):
        self.array=[None] * capacity
        self.size=0
    def insert(self,index,element):
        if index<0 or index>self.size:
            raise Exception('数组越界')
        if self.size>=len(self.array):
            Array.addcapacity(self)
        for i in range(self.size-1,index-1,-1):
            self.array[i+1]=self.array[i]
        self.size+=1
        self.array[index]=element
    def addcapacity(self):
        new_arrary=[None] * len(self.array) * 2
        for i in range(len(self.array)):
            new_arrary[i]=self.array[i]
        self.array=new_arrary
    def output(self):
        for i in self.array:
            if i is not None:
                print(i,'->',end='')
        print()
    def chu(self):
        for i in range(self.size):
             print(self.array[i]/self.array[0],i)
a=Array(5)
a.insert(0,1)
a.insert(1,1)
a.insert(2,2)
a.insert(3,3)



a.output()
print(a.chu())