mylist = [97, 23, 100, 88, 66, 84, 7, 21, 52, 17]
print("This is my list: ", mylist)


for element in range (len(mylist)):
    min_value = min(mylist[element:])
    min_index = mylist.index(min_value)
    mylist[element], mylist[min_index] = mylist[min_index], mylist[element]
print("New list after selection sort: ", mylist)

