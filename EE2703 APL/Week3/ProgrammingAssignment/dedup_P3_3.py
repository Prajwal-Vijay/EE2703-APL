def dedup(l):
    return list(dict.fromkeys(l).keys())
    
dedup([4, 2, 9, 4, 7, 2, 5])