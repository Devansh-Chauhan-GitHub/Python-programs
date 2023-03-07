class students:
    def input(self,a,n,r):
        self.age=a
        self.r=r
        self.n=n
    def output(self):
        print("Enter the Age : ",self.age)
        print("Enter the Rollno : ",self.r)
        print("Enter the Name : ",self.n)
s1=students()
s2=students()
ch=0
for i in range(0,2):
    a=input("Enter the Age of Person : ")
    n=input("Enter the Name of Person : ")
    r=input("Enter the Rollno. of Person : ")
    if ch==0:
        s1.input(a,n,r)
    if ch==1:
        s2.input(a,n,r)
    ch=ch+1
print("Enter the Student Data to be displsyed : ",end="")
i=int(input(""))
if i==1:
    s1.output()
elif i==2:
    s2.output()
print("************************End of Program************************")
