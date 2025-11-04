def sum_of_list_elements(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_of_list_elements(lst[1:])
