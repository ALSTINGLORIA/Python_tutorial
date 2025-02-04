
master_list = []

while True:
    num = int(input("Enter an integer to add to the list: "))
    master_list.append(num)
    yesOrNo = input("Do you want to add another number? (yes/no): ")
    if yesOrNo != "yes":
        break

threshold = int(input("Enter the threshold number: "))
new_list = []

for num in master_list:
    if num < threshold:
        new_list.append(num)

print("new list with numbers less than", threshold, ":", new_list)
