list1 = [1, 2, 3, 4, 5]
print(*list1)
print(list1, sep=" ")
list1.insert(len(list1), 6)
list1.append(7)
list1.extend([8,9,10,11])
list1.pop(4)
del list1[2]
print(list1)
list2 = ['A','B','C']

for x in list2:
    print(x)

list3 = ['Hello', 1 , True, 40.22]

list4 = [1, [2, 3], 4, 5]


