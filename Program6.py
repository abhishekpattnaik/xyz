class student:
    counter = 0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.counter=student.counter+1
    def msg(self):
        print(self.name)
        print(self.age)
    @classmethod
    def obj_count(cls):
        print(student.counter)
s1 = student("Abhishek",23)
s2 = student("Abhishek",23)
s3 = student("Abhishek",23)
s4 = student("Abhishek",23)
s1.msg()
s1.obj_count()