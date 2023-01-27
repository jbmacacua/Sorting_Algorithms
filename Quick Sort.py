def quicksort(numbers, left, right):
    if left < right:
        partition_pos = partition(numbers, left, right)
        quicksort(numbers, left, partition_pos - 1)
        quicksort(numbers, partition_pos + 1, right)

def partition(numbers, left, right):
    i = left
    j = right - 1
    pivot = numbers[right]

    while i < j:
        while i < right and numbers[i] < pivot:
            i += 1
        while j > left and numbers[j] >= pivot:
            j -= 1

        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            print("\t\t\t ", numbers)

    if numbers[i] > pivot:
        numbers[i], numbers[right] = numbers[right], numbers[i]
        print("\t\t\t ", numbers)
    return i

mylist = [97, 23, 100, 88, 66, 84, 7, 21, 52, 17]
print("\n-------------------------------------------------------------------------")
print("This is my list: ", mylist)
print("-------------------------------------------------------------------------\n")
quicksort(mylist, 0, len(mylist) - 1)
print("\n-------------------------------------------------------------------------")
print("New list after quick sort: ", mylist)
print("-------------------------------------------------------------------------")


