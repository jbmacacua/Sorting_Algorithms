def insertion_sort(mylist):
    for element in range(1, len(mylist)):
        val = mylist[element]
        ind = element - 1
        while ind >= 0 and val < mylist[ind]:
            mylist[ind + 1] = mylist[ind]
            ind = ind - 1
        mylist[ind + 1] = val
        print(mylist)

mylist = [97, 23, 100, 88, 66, 84, 7, 21, 52, 17]
print("\n-------------------------------------------------------------------------")
print("This is my list: ", mylist)
print("-------------------------------------------------------------------------\n")
insertion_sort(mylist)
print("\n-------------------------------------------------------------------------")
print("New list after insertion sort: ", mylist)
print("-------------------------------------------------------------------------")




