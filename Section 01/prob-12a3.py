from collections import deque

def rotate_list(lst, k):
    d = deque(lst)
    d.rotate(k)
    return list(d)
