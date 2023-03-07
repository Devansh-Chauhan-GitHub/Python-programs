import os
from time import sleep
a=int(input("Enter the number 1 : "))
b=int(input("Enter the number 2 : "))
cont='y'
sleep(2)
while(cont=='Y' or cont=='y'):
    os.system("cls")
    print("1.ADDITION - '+' ")
    print("2.SUBTRACTION - '-' ")
    print("3.MULTIPLICATION - '*' ")
    print("4.DIVISON - '/' ")
    ch=input("Enter the Choice : ")
    if(ch=='+'):
        print(a+b)
    elif(ch=='-'):
        print(a-b)
    elif(ch=='*'):
        print(a*b)
    elif(ch=='/'):
        print(a/b)
    cont=input("Do you want to Continue(Y/y) : ")
