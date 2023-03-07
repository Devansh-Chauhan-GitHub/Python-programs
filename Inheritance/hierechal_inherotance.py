class person_age:
    def set_details(self,age):
        self.age=age
    def op_details(self):
        print("AGE : ",self.age)
class person_gender(person_age):
    def set_details2(self,gender):
        self.gender=gender
    def op_details2(self):
        print("GENDER : ",self.gender)
class person(person_gender):
    def __init__(self,name,age,gender):
        self.name=name
        person_age.set_details(self,age)
        person_gender.set_details2(self,gender)
    def op_details3(self):
        print("NAME : ",self.name)
        person_age.op_details(self)
        person_gender.op_details2(self)
p1=person("ABC",18,"M")
p1.op_details3()