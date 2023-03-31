#defining the given values
cleaning_rate=60
cavity_filling=200
x_ray=100
tax_rate=0.15
disc1=0.05
disc2=0.1

#taking inputs from user 
name=input("enter the patient's name :  ")
cleaning=input("was cleaning performed ?(y/n) ")
cavity=input("was cavity filling done ? (y/n)")
xray=input("was xray done? (y/n) ")

#defining the functions
def calculate(name,cleaning,cavity,xray):
    if (cleaning=='y'):
        total=total+cleaning_rate
        print("you have done the cleaning")
    
