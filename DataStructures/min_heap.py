from heapq import heapify, heappush, heappop

class Minheap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1)//2
    
    def insertkey(self, k):
        heappush(self.heap, k)

    # it is assumed that the k is smaller than the value at i 
    def decreaseKey(self, i, k):
        self.heap[i] = k 
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def extract_min(self):
        return heappop(self.heap)
    
    def delete_key(self, i):
        self.decreaseKey(i, -999)
        self.extract_min()

    def print_heap(self):
        print(self.heap)

h = Minheap() 

h.print_heap()

h.insertkey(4)
h.insertkey(1)
h.insertkey(5)
h.insertkey(7)
h.insertkey(2)
h.insertkey(3)
h.insertkey(6)
h.insertkey(8)
h.insertkey(9)

h.print_heap()

h.delete_key(8)

h.print_heap()