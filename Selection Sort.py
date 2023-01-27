mylist = [97, 23, 100, 88, 66, 84, 7, 21, 52, 17]
print("This is my list: ", mylist)


for element in range (len(mylist)):
    min_value = min(mylist)
    min_index = mylist.index(min_value)
    mylist[0], mylist[min_index] = mylist[min_index], mylist[0]
