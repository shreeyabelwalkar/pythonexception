class AgeException(Exception):
    def __init__(self,age,msg="Age is not greater than equal to 18 years"):
        self.age=age
        self.message=msg
        super().__init__(self.message)
age = int(input("Enter the age of employee:"))
if age<18:
    raise AgeException(age)
else:
    print("You entered right age")






import sys
sys.exit()


dict = {101:"Sagar",102:"Poonam"}
print(dic[101])




import sys
sys.exit()

print(dir(locals()['__builtins__']))


import sys
sys.exit()


a=10
try:
    print(a/0)
except ArithmeticError as ae:
    print("cannot divide by zero")





import sys
sys.exit()

a=20
if a>10:
        pass