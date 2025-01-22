salary = int(input("enter your salary: "))
deduction = int(input("\n enter the deductable amount if any, else enter zero: "))

actualSalary = salary - deduction
print("\n current taxable amount:",actualSalary)

if(actualSalary <= 3_00_000):
    tax = 0
elif(actualSalary > 3_00_000 and actualSalary <= 7_00_000):
    tax = (actualSalary - 3_00_000) * 0.05
elif(actualSalary > 7_00_000 and actualSalary <= 10_00_000):
    tax = ((actualSalary - 7_00_000) * 0.10) + (3_00_000 * 0.05)
elif(actualSalary > 10_00_000 and actualSalary <= 12_00_000):
    tax = ((actualSalary - 10_00_000) * 0.15) + (7_00_000 * 0.10) + (3_00_000 * 0.05)
elif(actualSalary >12_00_000 and actualSalary <= 15_00_000):
    tax = tax = ((actualSalary - 12_00_000) * 0.20) + (10_00_000 * 0.15) + (7_00_000 * 0.10) + (3_00_000 * 0.05)
else:
    tax = tax = ((actualSalary - 15_00_000) * 0.20) + (12_00_000 * 0.30) + (10_00_000 * 0.15) + (7_00_000 * 0.10) + (3_00_000 * 0.05)

print("\n the amount of tax you have to pay is :",tax)