class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displaydetails(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
class student(person):
    def __init__(self,student_class,rollno,name,age):
        super().__init__(name,age)
        self.student_class=student_class
        self.rollno=rollno
    def student_displaydetails(self):
        person.displaydetails(self)
        print("Class of Student is :",self.student_class)
        print("Roll Number is :",self.rollno)
s1=student(1,1,"abc",5)
s1.student_displaydetails()