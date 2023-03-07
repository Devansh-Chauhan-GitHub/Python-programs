class person_age:
    def set_details(self,age):
        self.age=age
    def display_details(self):
        print("THE AGE IS : ",self.age)
class person_gender(person_age):
    def set_details1(self,gender,age):
        self.gender=gender
        self.age=age
    def display_details1(self):
        print("THE GENDER IS : ",self.gender)
class person(person_gender):
    def __init__(self,name,age,gender):
        self.name=name
        person_age.set_details(self,age)
        person_gender.set_details1(self,gender)
    def display_details2(self):
        print("THE NAME IS : ",self.name)
        person_age.display_details(self)
        person_gender.display_details1(self)
        person_
p1=person("AYUSH",10,"MALE")
p1.display_details2()