class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    #making push costly O(N) and making pop cheap O(1)
    def method1_push(self, val):
        while len(self.q1) != 0:
            self.q2.append(self.q1.pop(0))

        self.q1.append(val)

        while len(self.q2) != 0:
            self.q1.append(self.q2.pop(0))

    def method1_pop(self):
        return self.q1.pop(0)

    #making pop costly O(N) and push cheap O(1)
    def method2_push(self, val):
        self.q1.append(val)

    def method2_pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        ele = self.q1.pop(0)

        while len(self.q2) != 0:
            self.q1.append(self.q2.pop(0))

        return ele
    
if __name__ == '__main__':
    st = Stack()

    st.method2_push('a')
    st.method2_push('b')
    print(st.method2_pop())
    print(st.method2_pop())

    