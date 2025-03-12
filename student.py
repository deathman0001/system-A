class Student:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        print(self.name)

if __name__ == "__main__":
    student1 = Student('呂濰均')
    student2 = Student('施宇傑')
    
    student1.getName()
    student2.getName()