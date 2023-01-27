def merge_sort(elements):
    if len(elements) > 1:
        left_array = elements[:len(elements)//2]
        right_array = elements[len(elements)//2:]