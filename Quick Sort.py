def quicksort(numbers, left, right):
    if left < right:
        partition_pos = partition(numbers, left, right)
        quicksort(numbers, left, partition_pos - 1)
        quicksort(numbers, partition_pos + 1, right)

def partition(numbers, left, right):
    i = left
    j = right - 1
    pivot = numbers[right]



