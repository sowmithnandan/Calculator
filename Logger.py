from argparse import ArgumentError
import os
import math
# import colorama
# from colorama import Fore
from sys import platform
import os,signal
import logging

logging.basicConfig(level=logging.NOTSET,
                    filename="Calclogs.log",filemode="a",
                    format="%(asctime)s %(levelname)s-%(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S')

clear_cmd = ""
if platform == "linux" or platform == "linux2":
    clear_cmd = "clear"
elif platform == "win32":
    clear_cmd = "cls"

# print(clear_cmd)

class Calculator:
    def __init__(self):
        self.name = "Sceintific Calculator"
        logging.info(" [" + self.name + "]" + " Created a Calculator ")
    def sqrt(self,x):
        logging.info(" [" + self.name + "]" + " [SQRT] Getting Square Root of " + str(x))
        return math.sqrt(x)

    def factorial(self,x):
        logging.info(" [" + self.name + "]" + " [FACT] Getting factorial of " + str(x))
        return math.factorial(x)

    def log(self,x):
        logging.info(" [" + self.name + "]" + " [LOG] Getting Logaritm of " + str(x))
        return math.log(x)

    def pow(self,x,a):
        logging.info(" [" + self.name + "]" + " [POW] Getting power of " + str(x) + " ^ " + str(a))
        return math.pow(x,a)


    def BaseScreen(self):
        logging.info(" [" + self.name + "]" + " [BASESCREEN] Setting up Base Screen Terminal Template")
        print("Welcome to the Scientific Calculator")
        print("What do you want to do ?")
        print("● Square root function - √x")
        print("● Factorial function - x!")
        print("● Natural logarithm (base е) - ln(x)")
        print("● Power function - x")
        print("● Exit")

    def ChoiceMapping(self,choice,params):
        output = None
        if(choice == 1):
            if(len(params) < 1):
                logging.error(" [" + self.name + "]" + " [IPS] Insufficient Params Supplied")        
                raise ValueError("Insufficient Params Supplied")
                
            else:
                print(Fore.GREEN +"\n\nThe square root of " + str(params[0]) + " is " + str(self.sqrt(params[0])))
                output = self.sqrt(params[0])
        if(choice == 2):
            if(len(params) < 1):
                logging.error(" [" + self.name + "]" + " [IPS] Insufficient Params Supplied") 
                raise ValueError("Insufficient Params Supplied")
            else:
                print(Fore.GREEN +"\n\nThe factorial of " + str(params[0]) + " is " + str(self.factorial(params[0])))
                output = self.factorial(params[0])
        if(choice == 3):
            if(len(params) < 1):
                logging.error(" [" + self.name + "]" + " [IPS] Insufficient Params Supplied")        
                raise ValueError("Insufficient Params Supplied")
            else:
                print(Fore.GREEN + "\n\nThe natural logarithm of " + str(params[0]) + " is " + str(self.log(params[0])))
                output = self.log(params[0])
        if(choice == 4):
            if(len(params) < 2):
                logging.error(" [" + self.name + "]" + " [IPS] Insufficient Params Supplied")        
                raise ValueError("Insufficient Params Supplied")
            else:
                print(Fore.GREEN +"\n\nThe power of " + str(params[0]) + " to the power of " + str(params[1]) + " is " + str(self.pow(params[0],params[1])))
                output = self.pow(params[0],params[1])
        if(choice == 5):
            os._exit(0)

        print(Fore.RED + "\n\n\nPress Enter To Continue...\n\n\n")
        input()
        return output

    def take_input(self,params):
        try:
            # Convert it into integer
            for i in range(len(params)):
                params[i] = int(params[i])
            
            return params

        except ValueError:
            raise ValueError("Insufficient Params Supplied with unknown type of values")
        
    
    def TakeNumericalInput(self,choice):
        if(choice == 1 or choice == 2 or choice == 3):
            x = input("Enter a Number : ")
            params = self.take_input([x])
            return params

        if(choice == 4):
            x = input("Enter a Number : ")
            a = input("Enter the Power : ")
            params = self.take_input([x,a])
            return params

    def step(self):
        print(Fore.WHITE)
        self.BaseScreen()
        choice = int(input("Enter your choice: "))
        logging.info(" [" + self.name + "]" + " [CHS] Choice Selected : " + choice)        
        params = self.TakeNumericalInput(choice)
        logging.info(" [" + self.name + "]" + " [CHS] Params Selected : " + params)  
        # print(choice)
        self.ChoiceMapping(choice,params)
        os.system(clear_cmd)

    def loop(self):
        while True:
            self.step()