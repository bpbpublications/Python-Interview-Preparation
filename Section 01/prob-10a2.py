import heapq
 
def merge_sorted_lists(list1, list2):
    return list(heapq.merge(list1, list2))
