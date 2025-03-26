from student import Student
from teacher import Teacher
from password import PassWord

student1 = Student('呂潍均')
student2 = Student('蔡閎翔')
student3 = Student('施宇傑')
teacher1 = Teacher('A')
password1 = PassWord('A')

pass_acc = password1.getpassword()
if(pass_acc == 1):
    teacher1.getclass()



"""
student1.getName()
student2.getName()
student3.getName()
teacher1.getclass()
A01
b01 = Teacher('系統架構與軟體工程服務','朱紹威','4106','星期三','02 - 04')
b01.get()
"""