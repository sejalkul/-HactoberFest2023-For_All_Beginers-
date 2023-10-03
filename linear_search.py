def linear_Search(lists, n, key):  
  
    # Searching list sequentially using for
    for i in range(0, n):  
        if (lists[i] == key):    #if matches
            return i  
    return -1  
  
  
lists = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(lists)  
res = linear_Search(lists, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res) 
