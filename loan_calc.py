# get the loan details 
money_owed = float(input("How much money do you owe, in dollars?\n")) # $282,000
apr = float(input("What is your interest rate?\n")) # 2.25%
payment = float(input("What is your monthly payment?\n")) # $2,020
months = int(input("what is your loan duration?\n")) # 180

# divide apr by 100 to make it a percent and divide by 12 for monthly interest 
monthly_rate = apr/100/12 

for i in range(months):
    # Add interest
    interest_paid = round(money_owed*monthly_rate,2)
    money_owed = round(money_owed+interest_paid,2)

    if(money_owed - payment < 0):
        print("The last payment of your loan is $", money_owed)
        print("You paid off the loan in", i+1, "months")
        print("Hooray.. you paid off your loan, one step closer to being wealthy.. ")
        break

    # make payment
    money_owed = money_owed-payment

    print("Paid $", payment, " of which interest paid is $", interest_paid, ", Principal is $", payment - interest_paid, sep='',end = " ")
    print("Money still owed.. $", money_owed, sep='')