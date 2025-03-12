import os 

class Teacher:
    def __init__(self,course_name,name,code,day,time):
        self.name = name
        self.course_name = course_name
        self.code = code
        self.day = day
        self.time = time
        
    def get(self):
        print(self.course_name,self.name,self.code,self.day,self.time,end = '')


if __name__ == "__main__":
    teacher = Teacher('A','B','C','D','E')
    teacher.get()
