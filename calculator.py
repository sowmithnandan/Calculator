import math 

def FactorialFunc(n):
    Ans = 1 
    for i in range(2,n+1):
        Ans = Ans*i 
    return Ans 

while True:
    print("Enter you option:,your options are")
    print("1: Exit") 
    print("2: Square Root Function")
    print("3: Factorial Function") 
    print("4: Natural Logarithm ")
    print("5: Power Function")
    Choice = int(input())
    if Choice ==1:
        break
    elif Choice==2: 
        print("Enter your number:")
        Number1 = int(input())
        print("Result is:"+str(math.sqrt(Number1)))
    elif Choice==3:
        print("Enter your number:")
        Number1 = int(input())
        print("Result is:"+str(FactorialFunc(Number1)))
    elif Choice==4: 
        print("Enter your number:")
        Number1 = int(input())
        print("Result is:"+str(math.log(Number1))  )
    else: 
        print("Enter your number:")
        Number1 = int(input())
        print("Enter your number:")
        Number2 = int(input())
        print("Result is:"+str(pow(Number1,Number2)))   
print("Calculator Program has been forfeited");    





