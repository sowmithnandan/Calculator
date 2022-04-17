import math 
import logging

logging.basicConfig(level=logging.NOTSET,
                    filename="Calclogs.log",filemode="a",
                    format="%(asctime)s %(levelname)s-%(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S')

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
        logging.info("[MASTER] Options are printed on the users screen")
        print("Enter you option:your options are")
        print("1: Exit") 
        print("2: Square Root Function")
        print("3: Factorial Function") 
        print("4: Natural Logarithm ")
        print("5: Power Function")
        Choice = int(input())
        logging.info("[]Master] Init Calculator")
        if Choice ==1:
            break
        elif Choice==2: 
            print("Enter your number:")
            Number1 = int(input())
            logging.info("[SQRT] Getting Square Root of " + str(Number1))
            print("Result is:"+str(Calculator([Number1],Choice)))
        elif Choice==3:
            print("Enter your number:")
            Number1 = int(input())
            logging.info("[FACTORIAL] Getting the factorial of" + str(Number1))
            print("Result is:"+str(Calculator([Number1],Choice)))
        elif Choice==4: 
            print("Enter your number:")
            Number1 = int(input())
            logging.info("[NATLOG] Getting the logarithm of" + str(Number1))
            print("Result is:"+str(Calculator([Number1],Choice))  )
        elif Choice==5: 
            print("Enter your number:")
            Number1 = int(input())
            print("Enter your number:")
            Number2 = int(input())
            logging.info("[POW] Returning " + str(Number1) + " Raised to the power of "+ str(Number2))
            print("Result is:"+str(Calculator([Number1,Number2],Choice)))   
        else:
            logging.info("[MASTER] Unknown user input detected")
            print("Option not recognized")
            break
    print("Calculator Program has been forfeited");    





