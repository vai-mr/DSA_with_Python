from queue import PriorityQueue

def min_sum_digits(arr):
    n = len(arr)

    pq = PriorityQueue()

    num1 = ""
    num2 = ""

    for i in arr:
        pq.put(i)

    while not pq.empty():
        num1 += str(pq.get())
        if not pq.empty():
            num2 += str(pq.get())

    return int(num1) + int(num2)


if __name__ == '__main__':
    arr = [6, 8, 4, 5, 2, 3]
    print("minumum sum of digits: " , min_sum_digits(arr))