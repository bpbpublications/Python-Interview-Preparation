def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
 
    # Traverse both lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
 
    # Append remaining elements from list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
 
    # Append remaining elements from list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
 
    return merged_list
