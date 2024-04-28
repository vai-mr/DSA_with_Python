#implement queue using stack

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def method1_enqueue(self, val):     #costly enqueue O(n) cheap dequeue  O(1)
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
            

        self.s1.append(val)

        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def method1_dequeue(self):
        if len(self.s1) == 0:
            return "queue empty"
        else:
            return self.s1.pop()
        
    def method2_enqueue(self, val):        #costly dequeue O(n) cheap enqueue O(1)
        self.s1.append(val)

    def method2_dequeue(self):
        if len(self.s1) == 0: return "queue empty"
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())

        ele = self.s2.pop()

        while len(self.s2) !=0:
            self.s1.append(self.s2.pop())

        return ele
    

if __name__ == '__main__':
    q = Queue()
    q.method2_enqueue(2)
    q.method2_enqueue(3)
    print(q.method2_dequeue())

        
