import math 

def FactorialFunc(n):
    Ans = 1 
    for i in range(2,n+1):
        Ans = Ans*i 
    return Ans 


def Calculator(Input,Choice):
    if Choice==2:
        return  math.sqrt(Input[0])
    elif Choice==3:
        # Ans = Input[0]
        # for i in /range(2,Input[0]+1):
            # Ans = Ans*i 
        return FactorialFunc(Input[0])
    elif Choice==4:
        return math.log(Input[0])
    elif Choice==5:
        return pow(Input[0],Input[1])
    return 0  
if __name__ == '__main__':
    while True:
        print("Enter you option:your options are")
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
            print("Result is:"+str(Calculator([Number1],Choice)))
        elif Choice==3:
            print("Enter your number:")
            Number1 = int(input())
            print("Result is:"+str(Calculator([Number1],Choice)))
        elif Choice==4: 
            print("Enter your number:")
            Number1 = int(input())
            print("Result is:"+str(Calculator([Number1],Choice))  )
        elif Choice==5: 
            print("Enter your number:")
            Number1 = int(input())
            print("Enter your number:")
            Number2 = int(input())
            print("Result is:"+str(Calculator([Number1,Number2],Choice)))   
        else:
            print("Option not recognized")
            break
    print("Calculator Program has been forfeited");    





