import itertools
 
def flatten_list(nested_list):
    return list(itertools.chain(*nested_list))
