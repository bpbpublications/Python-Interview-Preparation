from collections import OrderedDict
 
def remove_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))
