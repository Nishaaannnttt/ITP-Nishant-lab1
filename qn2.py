#to take input 
def takeInput():
    num1=int(input("enter the first number: "))
    num2=int(input("enter the second number: "))
    operator=input("enter a desired operator :")
    return num1,num2,operator

def displayResult(num1,num2,operator):
    if(operator=='+'):
        sum=num1+num2
        print("the sum is :",sum)
    elif(operator=='-'):
        subtraction=num1-num2
        print("the subtraction is :",subtraction)
    
    