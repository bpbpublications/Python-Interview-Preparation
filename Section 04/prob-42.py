def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
 
        # Divide the array elements into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
 
        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)
 
        # Merge the sorted halves
        i = j = k = 0
 
        # Copy data to the temporary arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
 
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
