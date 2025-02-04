list1 = [23,56,2,99,58,30,87]
list2 = [67,23,65,98,34,56,7,19]

common_elements = []

for num in list1:
    if num in list2:
        common_elements.append(num)

print("Common elements between both lists:", common_elements)
