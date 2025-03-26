import os
import platform

from student import Student

password_save = {"1" : "1"}

class PassWord:
    def __init__(self, A):
        self.A = A
    def getpassword(self):
        A = 3
        while(A > 0):
            if(A != 3):
                print("還剩下%d次機會"%A)
            print("輸入帳號:",end="")
            account = input()
            print("輸入密碼:",end="")
            pssword = input()
            if account in password_save:
                if password_save[account] == pssword:
                    os.system('cls')
                    print("登錄成功")
                    return 1
            os.system('cls')
            print("登錄失敗")
            A -= 1    
        print("鎖住")
        return 0
if __name__ == "__main__":
    password = PassWord("A")
    password.getpassword()