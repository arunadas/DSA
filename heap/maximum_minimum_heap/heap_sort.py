def heap_sort(arr):   
    # create heap using given arr    
    def create_heap(arr):
        heap = []
        # assign 1st element
        heap.append(arr[0])
        i = 1        
        while i < len(arr):
            heap.append(arr[i])
            j = i 
            while j >= 0:
                # check with parent 
                k =  (j + 1)//2  - 1
                if heap[k] < heap[j] and k >= 0 :
                    #swap element
                    heap[k] , heap[j] = heap[j] , heap[k]
                j = k 
            i += 1    
        return heap 

    # delete heap and store the deleated element
    def delete_heap(heap):
        j = len(heap) - 1
        while j > 0:
            i = 0
            # remove head 
            head = heap[0]
            # move last element to head
            heap[0] = heap[j]  
            k = i
            # while children exists
            while ((2*k + 1) < j or (2*k + 2) < j) :
                if heap[2*k + 1] > heap[2*k + 2] :
                    if heap[2*k + 1] > heap[k]:
                        # swap with head
                        heap[2*k + 1] , heap[k] = heap[k] , heap[2*k + 1]
                        k = 2*k+1
                    else:
                        break    
                else:
                    if heap[2*k + 2] > heap[k]:
                        heap[2*k + 2] , heap[k] = heap[k] , heap[2*k + 2]
                        k = 2*k + 2
                    else:
                        break   
            # move removed head to last
            heap[j] = head
            j -= 1        
                       
        return heap
    # create heap
    print('array', arr)
    heap = create_heap(arr)
    print(heap)
    # delete heap
    sorted = delete_heap(heap)
    return sorted



arr = [10,20,15,30,40]
arr2 = [15,10,20,30,8,50,16]
print(heap_sort(arr2))