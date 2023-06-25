def rBinarySearch(l1, l,h, key):
    
    
    # find the minimum criteria
    if l == h:
        # check to find key
        if l1[l] == key:
            return l
        else:
            return 'Not Found'
        
    else:
        mid = (l + h ) // 2 
        if l1[mid] == key:
            # element found
            return mid
        elif  key < l1[mid]:
            return rBinarySearch(l1, l, mid - 1, key)
        else:
            return rBinarySearch(l1, mid + 1 , h , key)





l1 = [3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
l = 0
h = len(l1) - 1
key = 42
key2 = 30
print(rBinarySearch(l1, l, h, key))
