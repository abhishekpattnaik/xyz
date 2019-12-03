<<<<<<< HEAD
import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
=======
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
>>>>>>> 6746aa6d14a395c0321bc86e5e739422241c7dab
