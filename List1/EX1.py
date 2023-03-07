import os
a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
s=0
count='Y'
while count=='Y' or count=='y':
    os.system('cls')
    print("****************************MENU****************************")
    print("1. ADDITION '+'")
    print("2. SUBTRACTION '-'")
    print("3. MULTIPLICATION '*'")
    print("4. DIVISION '/'")
    ch=input("Enter the Choice : ")
    if ch=="+":
       s=a+b
    if ch=='-':
        s=a-b
    if ch=='*':
        s=a*b
    if ch=='/':
        s=a/b
    print(s)
    count=input("Do you want to continue (Y/y): ")