def swap(num, i, j):
    temp = num[i]
    num = num[:i] + num[j] + num[i + 1:]
    num = num[:j] + temp + num[j + 1:]
    return num

def reverse(num, i):
    j = len(num) - 1
    while (i < j):
        num = swap(num, i, j)
        i += 1
        j -= 1
    return num

def permutate(old_num):
    if(not old_num.isnumeric()): return 'NaN'
    i = len(old_num) - 2
    if(i < 0): return old_num
    while(i > 0 and old_num[i + 1] <= old_num[i]):
        i -= 1
    if (i > 0):
        j = len(old_num) - 1
        while (old_num[j] <= old_num[i]):
            j -= 1
        old_num = swap(old_num, i, j)
        return reverse(old_num, i + 1)
    return reverse(old_num, i)