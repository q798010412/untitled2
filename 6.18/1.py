class Student():
    def __init__(self, num, name, sex):
        self.num = num
        self.name = name
        self.sex = sex

    def study(self):
        print('爱学习')


a = Student(35, '张三', '男')
a.study()
print(a.name)
