salary = int(input("enter your salary: "))
deduction = int(input("\n enter the deductable amount if any, else enter zero: "))

actualSalary = salary - deduction
print("\n current taxable amount:",actualSalary)

if(actualSalary <= 2_50_000):
    tax = 0
elif(actualSalary > 2_50_000 and actualSalary <= 5_00_000):
    tax = (actualSalary - 2_50_000) * 0.05
elif(actualSalary > 5_00_000 and actualSalary <= 10_00_000):
    tax = ((actualSalary - 5_00_000) * 0.20) + (2_50_000 * 0.05)
elif(actualSalary > 10_00_000):
    tax = ((actualSalary - 10_00_000) * 0.30) + (5_00_000 * 0.20) + (2_50_000 * 0.05)

print("\n the amount of tax you have to pay is :",tax)