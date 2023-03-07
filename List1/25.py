a=0
s=0
per=0
a=[]
n=0
for i in range(0,5):
    print("Enter the Marks of Subject",i+1,":",sep=" ",end="")
    n=int(input())
    a.append(n)
print()
for i in a:
    s=s+i
per=((s/500)*100)
print("The percentage is :",per)
if per>=90 and per<=100:
    print("The grade is A.")
elif per>=80 and per<=90:
    print("The grade is B.")
elif per>=60 and per<=80:
    print("The grade is C.")
elif per>=50 and per<=60:
    print("The grade is D.")
elif per>=40 and per<=50:
    print("The grade is E.")
else:
    print("The grade is F.")
