#defining the given values
cleaning_rate=60
cavity_filling=200
x_ray=100
tax_rate=0.15
disc1=0.05
disc2=0.1

#taking inputs from user 
name=input("enter the patient's name :  ")
cleaning=input("was cleaning performed ? (y/n) ")
cavity=input("was cavity filling done ? (y/n)")
xray=input("was xray done? (y/n) ")

#defining the functions
def calculate(name,cleaning,cavity,xray):
    print("receipt for patients name is :",name)
    total=0
    if (cleaning=='y'):
        total=total+cleaning_rate
        print("you have done the cleaning")
    else:
        print("cleaning was not done ")
    if (cavity=='y'):
        total=total+cavity_filling
        print("cavity filling was done ")
    else:
        print("cavity filling was not done ")
    if(xray=='y'):
        total=total+x_ray
        print("x ray was done")
    else:
        print("x ray was not done ")
        
    #adding taxes
    tax=total*tax_rate
    print("your taxe amt is :",tax)
    total=tax+total
    
    #giving discount 
    if(total>200):
        discount1=total*disc1
        total=total-discount1
        print("your recieved 5 percent discount")
    elif(total>300):
        discount2=total*disc2
        total=total-discount2
        print("you received 10 per discount")
    else:
        print("no discount was received ")
    print("your total bill is :",total)
    
calculate(name,cleaning,xray,cavity)
        
        
    
        
