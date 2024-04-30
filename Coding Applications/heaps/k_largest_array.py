#program to print the k largest elements given an array of elements using minheap
#insert element into a heap
# if the size of heap exceeds k then pop the min element
# the final heap is the k largest elements

from heapq import heappush, heappop, heapify

def k_largest(arr, k, n):
    hq = []
    h_size = 0
    heapify(hq)

    for i in arr:
        heappush(hq, i)
        h_size += 1
        if h_size > k:
            heappop(hq)
            h_size -=1 

    print(hq)

arr = [11,3,2,1,15,5,4,45,88,96,50,45]
k_largest(arr, 3, len(arr))