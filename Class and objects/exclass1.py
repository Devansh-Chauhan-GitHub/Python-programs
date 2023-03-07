# Example of static method
# Allotment of an elective subject after validating the available choices:
class Choice:
    def __init__(self,n,r,subject):
        self.name=n
        self.roll=r
        self.subject=subject
    def display(self):
        print("------Student Information------")
        print("--> Name of Student:",self.name)
        print("--> RollNo. of Student:",self.roll)
        print("--> Subject Allotted :",self.subject)
    @staticmethod
    def validate_subject(subjects,x):
        if x in subjects:
            print("Option is available")
            return True
        else:
            print("Option is not available")
            return False
subjects=["DS", "CSA", "FOC", "OS", "TOC"]
sub=input("Enter the subject of your choice:")
if Choice.validate_subject(subjects,sub):
    name=input("Enter your Name:")
    roll=int(input("Enter your RollNo:"))
    c = Choice(name,roll,sub)
    c.display()