import heapq

li = [3,5,1,2,6]

heapq.heapify(li)

print("The created heap is: ", list(li))

heapq.heappush(li, 9)
print("The heap is: ", list(li))

heapq.heappop(li)
print("The heap is: ", list(li))

heapq.heappop(li)
print("The heap is: ", list(li))

heapq._heapify_max(li)
print("The created heap is: ", list(li))