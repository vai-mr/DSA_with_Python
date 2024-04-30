#to find the kth smallest number in a given array
#for max heap remember to push the elements in negative value
from heapq import heapify, heappop, heappush
def kth_smallest(arr, k):
    pq = []

    h_size = 0
    for i in arr:
        heappush(pq, -i)
        
        h_size +=1

        if h_size > k:
            heappop(pq)
            h_size -=1
    ele = heappop(pq)
    return -ele

arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
print(kth_smallest(arr, k))