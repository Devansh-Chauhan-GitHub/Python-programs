n=int(input("Enter The Value of n : "))
sum1=0
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    print(fact)
    sum=sum+fact
    fact=fact*i
    
print("Factorial of",n,": ",sum)