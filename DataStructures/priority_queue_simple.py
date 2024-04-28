class Pqueue:
    def __init__(self):
        self.q = []
        self.size = 0

    def enqueue(self, val):
        self.q.append(val)
        self.size +=1

    def dequeue(self):
        max = 0
        for i in range(self.size):
            if(self.q[i] > self.q[max]):
                max = i

        item = self.q[max]

        del self.q[max]
        return item
    
if __name__ == '__main__':
    pq = Pqueue()

    pq.enqueue(12)
    pq.enqueue(3)
    pq.enqueue(10)

    print(pq.dequeue())