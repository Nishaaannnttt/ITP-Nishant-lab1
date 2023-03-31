#defining the global variables 
PENNY_VALUE=1
NICKLE_VALUE=5
DIME_VALUE=10
QUARTER_VALUE=25
PENNIES_IN_DOLLAR=100

penny=int(input("enter the amount of pennies :"))
nickle=int(input("enter the amount of nickle :"))
dime=int(input("enter the amount of dimes :"))
quarter=int(input("enter the amount of quarters :"))

def calculation():
    total_penny= penny*PENNY_VALUE
    total_nickle=nickle*NICKLE_VALUE
    total_dime=dime*DIME_VALUE
    total_quarter=quarter*QUARTER_VALUE
    total_cents=total_nickle+total_penny+total_dime+total_quarter
    total_dollars=total_cents/PENNIES_IN_DOLLAR
    print("your total dollar is :",total_dollars)
    