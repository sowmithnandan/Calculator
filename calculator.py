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
        if (Input[0]>=0):
            return  math.sqrt(Input[0])
        else:
            logging.error("[SQRT] input less than zero")
            return -1
    elif Choice==3:
        if (Input[0]>=0):
            return FactorialFunc(Input[0])
        else:
            logging.error("[FACTORIAL] input less than zero")
            return -1
    elif Choice==4:
        if (Input[0]>0):
            return math.log(Input[0])
        else:
            logging.error("[NATLOG] input less than or equal to zero")
            return -1
    elif Choice==5:
        if Input[0]==0:
            logging.error("[POW] base is 0")
            return "Fail"
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
        try:     
            Choice = int(input())
            logging.info("[Master] Init Calculator")
            if Choice ==1:
                break
            elif Choice==2: 
                print("Enter your number:")
                Number1 = int(input())
                logging.info("[SQRT] Getting Square Root of " + str(Number1))
                result = Calculator([Number1],Choice)
                if result==-1:
                    print("Incorrect input for the selected option")
                    logging.info("[MASTER] Restarting Calculator ")
                    continue 
                print("Result is:"+str(result))
            elif Choice==3:
                print("Enter your number:")
                Number1 = int(input())
                logging.info("[FACTORIAL] Getting the factorial of" + str(Number1))
                result = Calculator([Number1],Choice)
                if result==-1:
                    print("Incorrect input for the selected option")
                    logging.info("[MASTER] Restarting Calculator ")
                    continue 
                print("Result is:"+str(result))
            elif Choice==4: 
                print("Enter your number:  ")
                Number1 = int(input())
                logging.info("[NATLOG] Getting the logarithm of" + str(Number1))
                result = Calculator([Number1],Choice)
                if result==-1:
                    print("Incorrect input for the selected option")
                    logging.info("[MASTER] Restarting Calculator ")
                    continue 
                print("Result is:"+str(result)  )
            elif Choice==5: 
                print("Enter your base:")
                Number1 = int(input())
                print("Enter your power:")
                Number2 = int(input())
                result = Calculator([Number1,Number2],Choice)
                if result=="Fail":
                    print("Incorrect input for the selected option")
                    logging.info("[MASTER] Restarting Calculator ")
                    continue 
                logging.info("[POW] Returning " + str(Number1) + " Raised to the power of "+ str(Number2))
                print("Result is:"+str(result ))   
            else:
                logging.error("[MASTER] Unknown user input detected, restarting calculator")
                print("Option not recognized")
        except:
            logging.error("[MASTER]Incorrect User Input detected")
            break
    logging.info("[MASTER] Calculator program terminated") 
    print("Calculator Program has been forfeited");    





