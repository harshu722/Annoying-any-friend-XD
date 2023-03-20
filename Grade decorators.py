class Student:  
    def __init__(self,name,grade):  
         self.name = name  
         self.grade = grade  
    @property  
    def display(self):  
         return self.name + " got grade " + self.grade  
  
stu = Student("John","B")  
print("Name:", stu.name)  
print("Grade:", stu.grade)  
print(stu.display)
