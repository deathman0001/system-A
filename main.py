# main.py
from teacher import Teacher
from student import Student

def main():
    # 創建教師物件
    teacher1 = Teacher("王老師", "數學")
    teacher2 = Teacher("朱老師", "英文")
    
    # 創建學生物件
    student1 = Student("呂濰均")
    student2 = Student("施宇傑")
    
    # 顯示教師資料
    teacher1.getName()
    teacher2.getName()

    # 學生選課
    student1.choose_course(teacher1)
    student2.choose_course(teacher2)

    # 顯示學生選的課程
    print(f"{student1.name} has enrolled in: {student1.courses}")
    print(f"{student2.name} has enrolled in: {student2.courses}")

if __name__ == "__main__":
    main()
