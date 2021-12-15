import random
lst = [random.randint(0,10000) for i in range(11)]
print(f'this is unsorted list \n {lst}')

def bubbleSorting(lst):

    for i in range(len(lst) - 1):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j + 1] :
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

res = bubbleSorting(lst)
print(f'List after sorting : \n {res}')