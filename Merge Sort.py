def merge_sort(elements):
    if len(elements) > 1:
        left_elements = elements[:len(elements)//2]
        right_elements = elements[len(elements)//2:]

        merge_sort(left_elements)
        merge_sort(right_elements)

        left_idx = 0
        right_idx = 0
        merge_idx = 0

        while left_idx < len(left_elements) and right_idx < len(right_elements):
            if left_elements[left_idx] < right_elements[right_idx]:
                elements[merge_idx] = left_elements[left_idx]
                left_idx += 1
            else:
                elements[merge_idx] = right_elements[right_idx]
                right_idx += 1
            merge_idx += 1

            while left_idx < len(left_elements):
                elements[merge_idx] = left_elements[left_idx]
                left_idx += 1
                merge_idx += 1
