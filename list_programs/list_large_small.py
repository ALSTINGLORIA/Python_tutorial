list = [23,35,2,90,17]
small,large = list[0], list[0]
for num in range(len(list)-1):
        if small > list[num+1]:
            small = list[num+1]
        if large < list[num+1]:
            large = list[num+1]

print("small:",small)
print("\nlarge:",large)