class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, data):
        self.stack.append(data)
        self.length +=1

    def pop(self):
        data = self.stack.pop()
        self.length -=1
        return data
    
    def top(self):
        return self.stack[-1]
    
    def print_stack(self):
        print(self.stack)


def infix_to_postfix(exp):

    def prec(c):
        if(c == '^'): return 3
        elif c == '/' or c == '*': return 2
        elif c == '+' or c == '-': return 1
        else: return -1

    result = []
    st = Stack()

    for i in range(len(exp)):
        c = exp[i]

        if('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'):
            result.append(c)
        elif c == '(':
            st.push(c)
        elif c == ')':
            while st.length > 0 and st.top() != '(':
                result.append(st.pop())
            st.pop()
        else:
            while st.length > 0 and (prec(c)<= prec(st.top())):
                result.append(st.pop())
            st.push(c)

    while(st.length > 0):
        result.append(st.pop())

    return ''.join(result)

def isOperator(c):
        if c in ['+','-','*','/','^','(',')']:
            return True
        return False

def prefix_to_infix(exp):
    
    st = Stack()
    i = len(exp) - 1
    while i >= 0:
        c = exp[i]
        if not isOperator(c):
            st.push(c)
            i -= 1
        else:
            str = "(" + st.pop() + c + st.pop() + ")"
            st.push(str)
            i -= 1

    return st.pop()

def postfix_to_infix(exp):
    
    st = Stack()
    i = 0
    exp_len = len(exp)
    while i < exp_len:
        c = exp[i]
        if not isOperator(c):
            st.push(c)
            i += 1
        else:
            op1 = st.pop()
            op2 = st.pop()
            str = "(" + op2 + c + op1 + ")"
            st.push(str)
            i += 1

    return st.pop()

def postfix_to_prefix(exp):
    
    st = Stack()
    exp_len = len(exp)

    for i in range(exp_len):
        if not isOperator(exp[i]):
            st.push(exp[i])
        else:
            op1 = st.pop()
            op2 = st.pop()
            str = f"{exp[i]}{op2}{op1}"
            st.push(str)


    result = ""
    while st.length > 0:
        result += st.pop()
    return result

def check_paranthesis(exp):
    def is_match(a,b):
        if a == '(' and b == ')': return True
        elif a == '{' and b == '}': return True
        return False
    
    st = Stack()
    exp_len = len(exp)
    for i in range (exp_len):
        if exp[i] in ['(', '{']: st.push(exp[i])
        elif exp[i] in [')','}']: 
            if st.length > 0 and is_match(st.top(), exp[i]): st.pop()
            else: return False

    if st.length == 0: return True
    return False

def eval(op1, op, op2):
    if op == '+':
        return int(op1) + int(op2)
    elif op == '-':
        return int(op1) - int(op2)
    elif op == '*':
        return int(op1) * int(op2)
    elif op == '/':
        return int(op1) / int(op2)
    
def eval_postfix(exp):
    st = Stack()

    exp_len = len(exp)
    for i in range(exp_len):
        if not isOperator(exp[i]):
            st.push(exp[i])
        else:
            op2 = st.pop()
            op1 = st.pop()
            res = eval(op1, exp[i], op2)
            st.push(res)

    return st.pop()

if __name__ == '__main__':
    st = Stack()
    st.push('b')
    st.push('a')
    st.push('c')
    st.push('d')
    st.print_stack()

    exp1 = '((A-(B/C))*((A/K)-L))'
    print(infix_to_postfix(exp1))

    exp2 = '*-A/BC-/AKL'
    print(prefix_to_infix(exp2))

    print(infix_to_postfix(prefix_to_infix(exp2)))

    exp3 = 'ABC/-AK/L-*'
    print(postfix_to_prefix(exp3))

    print(postfix_to_infix(exp3))

    exp4 = '{()}}'
    print(check_paranthesis(exp4))

    exp5 = "231*+9-"
    print(eval_postfix(exp5))