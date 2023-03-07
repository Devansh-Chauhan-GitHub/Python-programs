a=int(input("Enter the Year : "))
if(a%4==0) and (a%100!=0) or (a%400==0):
    print("The Year",a,"is a leap year.")
else:
    print("The Year",a,"is not a leap year.")
