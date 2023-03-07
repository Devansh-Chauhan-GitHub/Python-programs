class person:
    def setdetails(self,name,age):
        self.name=name
        self.age=age
    def displaydetails(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
class student(person):
    def student_setdetails(self,student_class,rollno):
        self.student_class=student_class
        self.rollno=rollno
    def student_displaydetails(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Gender : ",self.gender)
s1=student()
s1.setdetails("ABC",18)
s1.student_setdetails("A",1)
s1.displaydetails()
s1.student_displaydetails()