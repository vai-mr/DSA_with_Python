class Stack:
    def __init__(self):
        self.q = []
        self.size = 0

    def push(self, val):
        self.q.append(val)

        for i in range(self.size):
            self.q.append(self.q.pop(0))

        self.size +=1

    def pop(self):
        return self.q.pop(0)
    

if __name__ == '__main__':
    st = Stack()
    st.push('a')
    st.push('b')

    print(st.pop())
