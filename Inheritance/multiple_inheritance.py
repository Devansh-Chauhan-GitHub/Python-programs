class person_gender:
    def set_details(self,gender):
        self.gender=gender
    def display_details(self):
        print("Gender is :",self.gender)
class person_age:
    def set_details(self,age):
        self.age=age
    def display_details(self):
        print("The gender is :",self.gender)
        print("Age is :",self.age)
class person(person_age,person_gender):
    def __init__(self,name,age,gender):
        self.name=name
        person_age.set_details(self,age)
        person_gender.set_details(self,gender)
    def display_details(self):
        print("Name is :",self.name)
        person_age.display_details(self)
        person_gender.display_details(self)
p1=person("ABC",18,"M")
p1.display_details()