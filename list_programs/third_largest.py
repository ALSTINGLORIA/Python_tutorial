numbers = [21,33,98,45,27,12,4]

first = second = third = None

for num in numbers:
    if first is None or num > first:
        third = second
        second = first
        first = num
    elif second is None or num > second:
        third = second
        second = num
    elif third is None or num > third:
        third = num

print("Third largest:", third)
