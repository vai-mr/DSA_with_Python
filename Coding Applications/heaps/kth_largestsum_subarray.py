#Given an array of integers, write a program to find the kth largest sumof contiguous subarray within the array of numbers that has both negative and positive numbers

from heapq import heappush, heappop, heapify
def kth_largest_sum(arr, k, n):
    pre_sum = []
    pre_sum.append(0)
    pre_sum.append(arr[0])

    for i in range(2, n+1):
        pre_sum.append(pre_sum[i-1] + arr[i - 1])

    hq = []
    h_size = 0

    for i in range(1, n+1):
        for j in range(i, n+1):
            sub_array_sum = pre_sum[j] - pre_sum[i-1]

            if h_size < k:
                heappush(hq, sub_array_sum)
                h_size += 1
            else:
                if hq[0] < sub_array_sum:
                    heappop(hq)
                    heappush(hq, sub_array_sum)

    return heappop(hq)

arr = [10, -10, 20, -40]
n = len(arr)
k = 6
        
print(kth_largest_sum(arr, k, n))