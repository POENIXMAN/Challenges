
lst = [6802, 7316, 8275, 1681, 6875, 9401, 2363, 1387, 6349, 8644, 981]

def selectionSorting(lst):
    """Sorts in descending order"""
    for i in range(len(lst)):
        minvalue = i
        for j in range(i+1,len(lst)):
            if lst[j] > lst[minvalue]:
                minvalue = j
        lst[i], lst[minvalue] = lst[minvalue], lst[i]
    return lst    




def binary_search(arr, n):
	
    low = 0  
    high = len(arr) - 1  
    mid = 0  
  
    while low <= high:  
         
        mid = (high + low) // 2  
  
          
        if arr[mid] > n:  
            low = mid + 1  
    
        elif arr[mid] < n:  
            high = mid - 1  

        elif arr[mid] == n:
            return mid 
        
       
    return -1      
  
  
res = selectionSorting(lst)

result = binary_search(res, 8275)

print(result)