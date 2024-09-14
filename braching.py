      #calculate the total amount owed

first_rate_1000 =7.633
rate_over_1000 = 9.259

kw_hours = int(input("enter the kw hours owed"))

if kw_hours <= 1000:
    total=(kw_hours*first_rate_1000)/100
    print("amount owed is $" , total)

