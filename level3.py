import itertools

def find_min_size(lst):
    total = 0
    size = len(lst)-1

    while True:
        for i in xrange((size-1), 0, -1):
            total = total + lst[i]

        if total < lst[-1]:
            return size

        size = size-1
        total = 0

def count2(lst, size):
    ret = 0

    combs = list(itertools.combinations(lst, size))
    for comb in combs:
        total = 0
        for num in comb:
            total = total + num

        if total in lst:
            ret = ret +1

    return ret


def answer(lst):
    size = find_min_size(lst)
    total = 0
    
    for i in xrange(2, size+1):
        x = count2(lst, i)
        total = total + x

    return total
