import random
lst = [random.randint(0,10000) for i in range(11)]
print(f'this is unsorted list \n {lst}')

def selectionSorting(lst):
    for i in range(len(lst)):
        minvalue = i
        for j in range(i+1,len(lst)):
            if lst[j] > lst[minvalue]:
                minvalue = j
        lst[i], lst[minvalue] = lst[minvalue], lst[i]
    return lst    

res = selectionSorting(lst)
print(f'List after sorting : \n {res}')