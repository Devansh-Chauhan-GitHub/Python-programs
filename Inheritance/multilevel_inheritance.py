class person_gender:    
    def set_details(self,gender):
        self.gender=gender
    def output_details(self):
        print("Gender :",self.gender)
class person_age(person_gender):
    def set_details(self,age):
        self.age=age
    def output_details(self):
        print("Age :",self.age)
class person(person_age):
    def set_details(self,name,age,gender):
        person_gender.set_detaisl(self,gender)
        person_age.set_details(self,age)
        self.name=name
    def output_details(self):
        print("Name :",self.name)
        person_age.output_deatils(self)
        person_age.output_detils(self)
        person_age.output_details(self)
        person_age.output_details(self)
person.output_details("ABC","1","")
p1=person()
person.set_details("ABC",1,"M")
person.output_details("ABC",2,)
person.set_details("hello A : ")