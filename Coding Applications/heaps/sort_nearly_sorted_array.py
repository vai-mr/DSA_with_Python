#Given an array of Nelements, where each element is at most K away from its target position, devise algo which sorts in O(NlogK)

from heapq import heappush, heappop

def sort_nearly_sorted(arr, k):
    hq = []
    h_size = 0
    result = []
    for i in arr:
        heappush(hq, i)
        h_size += 1

        if h_size > k:
            result.append(heappop(hq))
            h_size -= 1

    while(hq):
        result.append(heappop(hq))

    print(result)

arr = [2, 6, 3, 12, 56, 8]
k = 3
sort_nearly_sorted(arr, k)