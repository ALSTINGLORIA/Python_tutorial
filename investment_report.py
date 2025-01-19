amount = int(input("enter the amount deposited: "))
intrestRate = int(input("enter the intrest rate: "))
time = int(input("enter the time in years: "))
print("%-20s %-20s %-20s %-10s " %("principal amount","interest rate","intrest amount","year"))

for years in range(1,time+1):
    si = (amount*intrestRate*years)/100
    print("%-20d %-20d %-20d %-10d" %(amount,intrestRate,si,years))    