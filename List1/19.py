a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
c=int(input("Enter number 3 : "))
if(a>b) and (a>c):
    print("The number",a,"is greatest.")
elif(b>c):
    print("The number",b,"is greatest.")
else:
    print("The number",c,"is greatest.")
