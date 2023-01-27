def insertion_sort(mylist):
    for element in range(1, len(mylist)):
        val = mylist[element]
        ind = element - 1
        while ind >= 0 and val < mylist[ind]:
            mylist[ind + 1] = mylist[ind]
            ind = ind - 1
        mylist[ind + 1] = val
        print(mylist)


