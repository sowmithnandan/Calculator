#include<iostream> 
#include <cmath>
using namespace std; 

long long int Factorial(long long int n)
    {
    long long int fact=1;
    for(int i=2;i<=n;i++)
        {
        fact *= i;
        }
    return fact;
    }

int main()
    {
    while(true)
        {
        int Choice;
        long long Input,Pow;

        cout<<"Choose what you want to do:"<<endl;
        cout<<"1: exit"<<endl;
        cout<<"2: Square root function "<<endl;
        cout<<"3: Factorial function"<<endl;
        cout<<"4: Natural logarithm"<<endl;
        cout<<"5: Power Function"<<endl;
        cin>>Choice;
        if(Choice==1)
            {
            cout<< "Calculator program has been forfeited"<<endl;
            break;
            }  
        else if (Choice==2)
            {
            cout<<"Enter your input:"<<endl;
            cin>>Input;
            cout<<pow(Input,0.5)<<endl;
            }
        else if(Choice==3)
            {
            cout<<"Enter your input:"<<endl;
            cin>>Input;
            cout<<Factorial(Input)<<endl;
            }
        else if(Choice==4)
            {
            cout<<"Enter your input:"<<endl;    
            cin>>Input;
            cout<<log(Input)<<endl;
            }
        else if(Choice==5)
            {
            cout<<"Enter your input:"<<endl;     
            cin>>Input;
            cout<<"Enter your input:"<<endl;
            cin>>Pow; 
            cout<<pow(Input,Pow)<<endl;
            }     
        }
    return 0;
    }