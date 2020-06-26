class Array():
    def __init__(self,capacity):
        self.array=[None] * capacity
        self.size=0
    def insert(self,index,element):
        '''

        :param index:
        :type index:
        :param element:
        :type element:
        :return:
        :rtype:
        '''
        if index<0 or index>self.size:
            raise Exception('数组越界')
        if index>=len(self.array):
            Array.addcapacity(self)
        for i in range(self.size-1,index-1,-1):
            self.array[i+1]=self.array[i]
        self.size+=1
        self.array[index]=element

    def addcapacity(self):
        new_array=[None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i]=self.array[i]
        self.array=new_array
    def output(self):

        for i in range(self.size):
            print(self.array[i],'->',end='')
        print()
    def remove(self,delindex):
        if delindex<0 or delindex>self.size:
            raise Exception('数组越界')
        for i in range(delindex,self.size-1):
            self.array[i]=self.array[i+1]
        self.size-=1
test=Array(4)
test.insert(0,0)
test.insert(1,1)
test.insert(2,2)
test.insert(3,3)
test.remove(3)
test.output()
"""
Author:Mr.Qi
Create:2020/6/19 10:16
"""

