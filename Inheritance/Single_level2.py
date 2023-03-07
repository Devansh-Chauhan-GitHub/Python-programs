class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displaydetails(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
class student(person):  
    def __init__(self,student_class,rollno):
        super().__init__("II")
        self.student_class=student_class       
        self.rollno=rollno
        person.displaydetails(self)
        print("Class of Student is :",self.student_class)
        print("Roll Number is :",self.rollno)
s1=student("ABC",18)
s2=student("ABC",18,"M","A")
s3=student("PQR",18,"M","A")
s1.student_displaydetails("abc",18,"M")
s1.student__init__("abc",18,"M","A")