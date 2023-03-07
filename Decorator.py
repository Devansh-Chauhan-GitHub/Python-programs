class students:
    def __init__(self,a,n,r):
        self.a=a
        self.n=n
        self.r=r
    def output(self):
        print("AGE : ",self.a)
        print("NAME : ",self.n)
        print("ROLLNO : ",self.r)
s1=students(18,"abc",1)
s2=students(18,"xyz",2)
s3=students(18,"pqr",3)
s1.output()
s2.output()
s3.output()