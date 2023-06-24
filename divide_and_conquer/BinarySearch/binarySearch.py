def binSearch(l1, key):
    l = 0
    h = len(l1) - 1

    while (l <= h):

        mid = (l + h)//2

        if key == l1[mid]:
            return mid 
        elif key < l1[mid]:
            h = mid - 1 
        else:
            l = mid + 1

    return 'Not Found'


l1 = [3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
key1 = 42
key2 = 12
key = 30

print(binSearch(l1,key))