class schoolmember():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class teacher(schoolmember):
    count=0
    def __init__(self,name,age,salary):
        schoolmember.__init__(self,name,age)
        self.salary=salary
        count=count+1
        print("Account updated for ",self.name)
    @classmethod
    def no_of_teachers(cls):
        print(count)
class student(schoolmember):
    def __init__(self,name,age,marks):
        schoolmember.__init__(self,name,age)
        self.marks=marks
        print("Account updated for ",self.name)
class staff(schoolmember):
    def __init__(self,name,age,group):
        schoolmember.__init__(self,name,age)
        self.group=group
        print("Account updated for ",self.name)
t=teacher("Abhishek",23,37000)
t.no_of_teachers()