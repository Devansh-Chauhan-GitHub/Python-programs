pas=input("Enter the Password : ")
low=0
dig=0
up=0
sp=0
l=0
lp=0
count=0
l=len(pas)
for i in pas:
    if(low<1) and (i.islower()):
        low=low+1
    if (dig<1) and (i.isdigit()):
       dig=dig+1
    if (up<1) and (i.isupper()):
        up=up+1
    if (sp<1) and (i in "@#$"):
        sp=sp+1
count=low+dig+up+sp
if(l<12 and l>6 and count==4):
    print("The Password can be Accepted.")
else:
    print("The Password can not be Accepted.")