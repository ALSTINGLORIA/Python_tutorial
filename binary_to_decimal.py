num = input("enter the number in binary: ")
decimal = 0
power = len(num)-1
for digit in num: 
    decimal += ((int(digit)) * (2**power))
    print((2**power),"\n")
    power = power - 1 

print("the decimal value is:",decimal)