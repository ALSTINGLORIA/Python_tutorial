
master_list = []

while True:
    num = int(input("Enter an integer to add to the list: "))
    master_list.append(num)
    more = input("Do you want to add another number? (y/n): ")
    
    if more != "y":
        break

even_list = []

for num in master_list:
    if num % 2 == 0:
        even_list.append(num)

even_list.sort()

print("Even numbers in ascending order:", even_list)
