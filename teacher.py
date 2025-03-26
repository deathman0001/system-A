from student import Student

class Teacher:
    def __init__(self):

    def getclass(self):
        teacher_name_list = ['王老師', '朱老師', '陳老師']
        teacher_list = []  # Define the teacher_list here
        for i in range(len(teacher_name_list)):
            teacher = Student(teacher_name_list[i])
            teacher_list.append(teacher)
        print(teacher_list)

        print("--------------------------------")
        for i in range(len(teacher_name_list)):
            print(str(i), ':', teacher_name_list[i])
        print("--------------------------------")
        print("輸入:",end="")
        a = input()
        return a

if __name__ == "__main__":
    # Provide a name when creating the Teacher instance
    teacher = Teacher()
    teacher.getclass()  # Correct method name (was `get()`, now `getclass()`)
