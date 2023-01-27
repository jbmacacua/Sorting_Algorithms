mylist = [97, 23, 100, 88, 66, 84, 7, 21, 52, 17]
print("\n-------------------------------------------------------------------------")
print("This is my list: ", mylist)
print("-------------------------------------------------------------------------\n")


for elements in range(len(mylist)-1):
    for element in range (len(mylist)-1):
        if mylist[element] > mylist[element+1]:
            mylist[element], mylist[element+1] = mylist[element+1], mylist[element]
            print(mylist)
        else:
            print(mylist)
print("\n-------------------------------------------------------------------------")
print("New list after bubble sort: ", mylist)
print("-------------------------------------------------------------------------")
