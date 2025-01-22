num = int(input("enter a number:"))
test = num
while(True):
    check = 0.5 * (test + (num/test))
    if abs(check - test) == 0:
        break
    test = check

print("the square root of",num,"is",check)