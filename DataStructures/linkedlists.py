class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node

    def insert_after(self, old_data, new_data):
        cur = self.head

        new_node = Node(new_data)
        while(cur is not None):
            if(cur.data == old_data):
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next

    def append(self,new_data):
        cur = self.head
        while(cur.next is not None):
            cur = cur.next

        new_node = Node(new_data)
        new_node.next = cur.next
        cur.next = new_node

    def print_list(self):
        cur = self.head

        while(cur is not None):
            print(f"{cur.data} -- ", end=" ")
            cur = cur.next
        print("\n")

    def del_beginning(self):
        temp = self.head
        self.head = temp.next
        del temp

    def pop(self):
        prev = self.head
        cur = self.head
        while(cur.next is not None):
            prev = cur
            cur = cur.next
        
        prev = cur.next
        del cur

    def del_pos(self, pos):
        cur = self.head
        prev = self.head


        for i in range(0, pos):
            if i == 0 and pos == 1:
                self.head = self.head.next
                del cur
            else:
                if i == pos -1 and cur is not None:
                    prev.next = cur.next
                    del cur
                else:
                    prev = cur
                    if prev is None:
                        return
                    cur = cur.next

    def del_index(self, ind):
        if self.head is None:
            return
        
        cur = self.head
        prev = self.head
            

        i = 0 
        while cur.next and i < ind:
            prev = cur
            cur = cur.next
            i +=1

        if i < ind:
            return
        elif ind == 0:
            self.head = cur.next
            del cur
        else:
            prev.next = cur.next
            del cur
        
    def search(self, data):
        cur = self.head
        while(cur):
            if cur.data == data:
                return True
            cur = cur.next
        return False
    
    def get_count(self):
        cur = self.head
        count = 0
        while(cur):
            count += 1
        return count
    
    def get_count_rec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_count_rec(node.next)
        
    # def get_count_rec(self, node, count = 0): #tail recurssion
    #     if not node:
    #         return count
    #     else:
    #         return self.get_count_rec(node.next, count+1)
        

    def get_count_rec_call(self):
        return self.get_count_rec(self.head)
    
    def reverse_ll(self):
        cur = self.head
        prev = None
        next = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev

    def print_nth_fromlast(self, ptr, n):
        i = 0
        if not ptr:
            return i
        i = self.print_nth_fromlast(ptr.next, n)
        i+=1
        if ( i == n):
            print(ptr.data)
        return i

    def del_list(self):
        cur = self.head
        while cur:
            self.head = cur.next
            del cur
            cur = self.head

if __name__ == "__main__":
    ll = LinkedList()
    ll.push('a')
    ll.print_list()
    ll.insert_after('a', 'b')
    ll.print_list()
    ll.append('c')
    ll.append('d')
    ll.append('e')
    ll.print_list()
    ll.del_pos(1)
    ll.print_list()
    ll.del_index(0)
    ll.print_list()
    ll.reverse_ll()
    ll.print_list()
    ll.print_nth_fromlast(ll.head, 3)
    ll.del_list()
    ll.print_list()
