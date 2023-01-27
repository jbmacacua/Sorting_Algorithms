def merge_sort(elements):
    if len(elements) > 1:
        left_elements = elements[:len(elements)//2]
        right_elements = elements[len(elements)//2:]

        merge_sort(left_elements)
        merge_sort(right_elements)

        left_idx = 0
        right_idx = 0
        merge_idx = 0