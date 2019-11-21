class schoolmember():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("Name :",self.name)
        print("Age :",self.age)
class teacher(schoolmember):
    def __init__(self,name,age,salary):
        schoolmember.__init__(self,name,age)
        self.salary=salary
        print("Account updated for: ",self.name)
    def info(self):
        schoolmember.info(self)
        print("Salary: ",self.salary)
class student(schoolmember):
    def __init__(self,name,age,marks):
        schoolmember.__init__(self,name,age)
        self.marks=marks
        print("Account updated for: ",self.name)
    def info(self):
        schoolmember.info(self)
        print("Marks :",self.marks)
t = teacher("Prafulla",60,1000000)
s = student("Abhishek",23,100)
l = [t,s]
for i in l:
    i.info()
    print()
print("Thank you")